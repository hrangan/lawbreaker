#!/usr/bin/env python
import os
import sys
import json

from collections import OrderedDict
from bottle import route, run, template, static_file

from lawbreaker.character import Character
from lawbreaker.names import Name


@route('/')
def main():
    character = Character(name=Name.get())
    return template('web/templates/index', content=json.loads(repr(character), object_pairs_hook=OrderedDict))


@route('/static/<path:path>')
def callback(path):
    return static_file(path, root=os.path.abspath(os.path.split(sys.argv[0])[0])+'/static')


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host='localhost', port=8080, reloader=True, debug=True)
