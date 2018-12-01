#!/usr/bin/env python
import os
import sys
import json

from collections import OrderedDict
from urllib2 import urlopen, HTTPError
from bottle import route, run, template, static_file, request, response, redirect, hook

from lawbreaker.character import Character
from lawbreaker.names import Name
from lawbreaker.database import Database
from lawbreaker.exceptions import NoResultsFound
from lawbreaker.utils import spawn_daemon


db = Database()
static_root = os.path.abspath(os.path.split(sys.argv[0])[0]) + '/static'


if os.environ.get('APP_LOCATION') == 'heroku':
    @hook('before_request')
    def ssl_redirect():
        """ Redirect incoming http requests to https

            This doesn't work on a local server since there are no SSL
            certificates.
        """
        if request.get_header('X-Forwarded-Proto', 'http') != 'https':
            redirect(request.url.replace('http://', 'https://', 1), code=301)

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
                print 'Polling https://lawbreaker.herokuapp.com/keep_awake'
                urlopen("https://lawbreaker.herokuapp.com/keep_awake")
            except HTTPError:
                pass
        spawn_daemon(keep_awake, interval=25*60)


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
