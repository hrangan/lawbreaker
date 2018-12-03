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
    def before_request():
        if request.headers.get('X-Forwarded-Proto', 'http') != 'https':
            return redirect(request.url.replace('http://', 'https://', 1), code=301)

    spawn_daemon(lambda: db.clear_expired(), interval=12*60*60)  # Runs every 12 hours

    if os.environ.get('KEEP_AWAKE', 'false').lower() == 'true':
        def keep_awake():
            print('Polling https://lawbreaker.herokuapp.com/keep_awake')
            get("https://lawbreaker.herokuapp.com/keep_awake")
        spawn_daemon(keep_awake, interval=25*60)


@app.route('/')
def generate_random():
    character = Character(name=Name.get())
    character_json = repr(character)
    db.insert(character.id, character_json)
    return render_template('index.html',
                           content=json.loads(character_json,
                                              object_pairs_hook=OrderedDict),
                           permalink=False)


@app.route('/<character_id>')
@app.route('/<character_id>/')
def fetch_by_id(character_id):
    try:
        character_json = db.select(character_id)
    except NoResultsFound:
        abort(404)

    return render_template('index.html',
                           content=json.loads(character_json,
                                              object_pairs_hook=OrderedDict),
                           permalink=True)


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


def main():
    if os.environ.get("APP_LOCATION") == "heroku":
        serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        app.run(host="localhost", port=5000, debug=True)


if __name__ == '__main__':
    main()
