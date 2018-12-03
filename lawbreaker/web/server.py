#!/usr/bin/env python
import os
import json

from collections import OrderedDict

from requests import get as requests_get
from flask import Flask, render_template, abort, request, redirect

from lawbreaker.character import Character
from lawbreaker.names import Name
from lawbreaker.exceptions import NoResultsFound
from lawbreaker.web.database import Database
from lawbreaker.web.utils import spawn_daemon

from waitress import serve

app = Flask(__name__)
db = Database()


if os.environ.get('APP_LOCATION') == 'heroku':
    @app.before_request
    def before_request():
        if request.headers.get('X-Forwarded-Proto', 'http') != 'https':
            return redirect(request.url.replace('http://', 'https://', 1), code=301)

    spawn_daemon(lambda: db.clear_expired(),
                 interval=12*60*60)  # Runs every 12 hours

    if os.environ.get('KEEP_AWAKE', 'false').lower() == 'true':
        print('Polling https://lawbreaker.herokuapp.com/keep_awake')
        spawn_daemon(requests_get("https://lawbreaker.herokuapp.com/keep_awake"),
                     interval=25*60)


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
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


if __name__ == '__main__':
    main()
