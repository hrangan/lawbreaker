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
    """
    Names courtesy of
    https://www.reddit.com/r/DnDBehindTheScreen/comments/50pcg1/a_post_about_names_names_for_speakers_of_the/
    """
    character = Character(name=Name.get())
    return template('templates/index', content=json.loads(repr(character), object_pairs_hook=OrderedDict))


@route('/static/<path:path>')
def callback(path):
    return static_file(path, root=os.path.abspath(os.path.split(sys.argv[0])[0])+'/static')


if __name__ == '__main__':
    run(host='0.0.0.0', port=7986, reloader=True, debug=True)
