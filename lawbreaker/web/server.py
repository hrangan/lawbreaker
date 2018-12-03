#!/usr/bin/env python
import os
import sys
import json

from collections import OrderedDict
from urllib.request import urlopen
from urllib.error import HTTPError
from flask import Flask, render_template, abort, request, redirect

from lawbreaker.character import Character
from lawbreaker.names import Name
from lawbreaker.exceptions import NoResultsFound
from lawbreaker.web.database import Database
from lawbreaker.web.utils import spawn_daemon

from waitress import serve

app = Flask(__name__)
db = Database()
static_root = os.path.abspath(os.path.split(sys.argv[0])[0]) + '/static'


if os.environ.get('APP_LOCATION') == 'heroku':
    @app.before_request
    def before_request():
        if request.headers.get('X-Forwarded-Proto', 'http') != 'https':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

    def clear_expired():
        db.clear_expired()
    spawn_daemon(clear_expired, interval=12*60*60)  # Runs every 12 hours

    if os.environ.get('KEEP_AWAKE', 'false').lower() == 'true':
        def keep_awake():
            """ Keep-awake polling

                Sets up a daemon that polls https://lawbreaker.herokuapp.com
                every 25 minutes to stop the dyno from sleeping. An invalid URL
                is used so that the full character creation process does not
                run.
            """
            try:
                print('Polling https://lawbreaker.herokuapp.com/keep_awake')
                urlopen("https://lawbreaker.herokuapp.com/keep_awake")
            except HTTPError:
                pass
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
    return render_template('error404.html'), 404


def main():
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


if __name__ == '__main__':
    main()
