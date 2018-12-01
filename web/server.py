#!/usr/bin/env python
import os
import time
import sys
import json
import urllib2
import threading

from collections import OrderedDict
from datetime import datetime, timedelta
from bottle import route, run, template, static_file, request, response, redirect, hook

from lawbreaker.character import Character
from lawbreaker.names import Name
from lawbreaker.database import Database
from lawbreaker.exceptions import NoResultsFound


db = Database()
static_root = os.path.abspath(os.path.split(sys.argv[0])[0]) + '/static'


if os.environ.get('APP_LOCATION') == 'heroku':
    # SSL Redirection
    # This doesn't work locally since there is no SSL certificate
    @hook('before_request')
    def ssl_redirect():
        """Redirect incoming http requests to https"""
        if request.get_header('X-Forwarded-Proto', 'http') != 'https':
            redirect(request.url.replace('http://', 'https://', 1), code=301)

    if os.environ.get('KEEP_AWAKE', 'false').lower() == 'true':
        # Keep-awake polling
        # Sets up a daemon that polls https://lawbreaker.herokuapp.com every 25
        # minutes to stop the dyno from sleeping
        def keep_awake():
            last_run = datetime.now()
            while True:
                if datetime.now() - last_run > timedelta(seconds=25*60):
                    print 'Polling https://lawbreaker.herokuapp.com to keep it awake'
                    urllib2.urlopen("https://lawbreaker.herokuapp.com")
                    last_run = datetime.now()
                time.sleep(60)

        thread = threading.Thread(target=keep_awake)
        thread.daemon = True
        thread.start()


@route('/')
def generate_random():
    character = Character(name=Name.get())
    character_json = repr(character)
    db.insert(character.id, character_json)
    return template('web/templates/index',
                    content=json.loads(character_json, object_pairs_hook=OrderedDict))


@route('/<character_id>')
def fetch_by_id(character_id):
    try:
        character_json = db.select(character_id)
    except NoResultsFound:
        response.status = 404
        return template('web/templates/error404')

    return template('web/templates/index',
                    content=json.loads(character_json, object_pairs_hook=OrderedDict),
                    permalink=True)


@route('/static/<path:path>')
def static_files(path):
    return static_file(path, root=static_root)


@route('/favicon.ico')
def favicon():
    return static_file('/favicon.ico', root=static_root)


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(server="waitress", host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(server="waitress", host='localhost', port=5000, reloader=True, debug=True)
