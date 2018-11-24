#!/usr/bin/env python
import os
import sys
import json

from collections import OrderedDict
from bottle import route, run, template, static_file, request, response

from lawbreaker.character import Character
from lawbreaker.names import Name
from lawbreaker.database import Database
from lawbreaker.exceptions import NoResultsFound


db = Database()


@route('/')
def main():
    character = Character(name=Name.get())
    character_json = repr(character)
    db.insert(character.id, character_json)
    return character_json if 'application/json' in request.headers.get('Accept', '') \
        else template('web/templates/index', content=json.loads(character_json, object_pairs_hook=OrderedDict))


@route('/favicon.ico')
def favicon_fallback():
    return callback('/favicon.ico')


@route('/<character_id>')
def fetch_by_id(character_id):
    try:
        character_json = db.select(character_id)
    except NoResultsFound:
        response.status = 404
        return None if ('application/json' in request.headers.get('Accept', '')) \
            else template('web/templates/error404')

    return character_json if ('application/json' in request.headers.get('Accept', '')) \
        else template('web/templates/index',
                      content=json.loads(character_json, object_pairs_hook=OrderedDict),
                      permalinked=True)


@route('/static/<path:path>')
def callback(path):
    return static_file(path, root=os.path.abspath(os.path.split(sys.argv[0])[0])+'/static')


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, reloader=True, debug=True)
