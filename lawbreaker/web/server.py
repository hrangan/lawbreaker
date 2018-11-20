#!/usr/bin/env python
import os
import sys
import json

from collections import OrderedDict
from bottle import route, run, template, static_file

from lawbreaker.character import Character


@route('/')
def main():
    character = Character(name=" ")
    return template('templates/index', content=json.loads(repr(character), object_pairs_hook=OrderedDict))


@route('/static/<path:path>')
def callback(path):
    return static_file(path, root=os.path.abspath(os.path.split(sys.argv[0])[0])+'/static')


if __name__ == '__main__':
    run(host='0.0.0.0', port=7986, reloader=True, debug=True)
