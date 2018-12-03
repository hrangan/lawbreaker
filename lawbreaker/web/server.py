#!/usr/bin/env python
import os
import json

from collections import OrderedDict

from requests import get
from flask import Flask, render_template, abort, request, redirect

from lawbreaker.character import Character
from lawbreaker.names import Name
from lawbreaker.exceptions import NoResultsFound
from lawbreaker.web.database import Database
from lawbreaker.web.utils import spawn_daemon

from waitress import serve

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = Database()


if os.environ.get('APP_LOCATION') == 'heroku':
    @app.before_request
    def ssl_redirect():
        """ Redirect incoming http requests to https
            This doesn't work on a local server since there are no SSL
            certificates.
        """
        if request.headers.get('X-Forwarded-Proto', 'http') != 'https':
            return redirect(request.url.replace('http://', 'https://', 1), code=301)

    spawn_daemon(lambda: db.clear_expired(), interval=12*60*60)  # Runs every 12 hours

    if os.environ.get('KEEP_AWAKE', 'false').lower() == 'true':
        def keep_awake():
            """ Polls https://lawbreaker.herokuapp.com/keep_awake every 25
                minutes to stop the dyno from sleeping. An invalid URL is used
                so that the full character creation process is not run.
            """
            print('Polling https://lawbreaker.herokuapp.com/keep_awake')
            get("https://lawbreaker.herokuapp.com/keep_awake")
        spawn_daemon(keep_awake, interval=25*60)


@app.after_request
def security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = (
                                                   "default-src 'none'; "
                                                   "font-src 'self' https://fonts.gstatic.com data;"
                                                   "img-src 'self';"
                                                   "object-src 'none';"
                                                   "script-src 'none';"
                                                   "style-src 'self' https://fonts.googleapis.com;"
                                                   "frame-ancestors 'self'"
                                                   )
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'no-referrer'
    return response


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.route('/')
def generate_random():
    character = Character(name=Name.get())
    character_json = repr(character)
    db.insert(character.id, character_json)
    return render_template('index.html', content=json.loads(character_json, object_pairs_hook=OrderedDict))

@app.route('/<character_id>/')
@app.route('/<character_id>')
def fetch_by_id(character_id):
    try:
        character_json = db.select(character_id)
    except NoResultsFound:
        abort(404)
    return render_template('index.html',
                           content=json.loads(character_json, object_pairs_hook=OrderedDict),
                           permalink=True)


def main():
    if os.environ.get("APP_LOCATION") == "heroku":
        serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        app.run(host="localhost", port=5000, debug=True)


if __name__ == '__main__':
    main()
