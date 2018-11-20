#!/usr/bin/env python
from lawbreaker.character import Character
from bottle import route, run, template, static_file
import os
import sys


@route('/')
def main():
    char = Character(name=" ")
    return template('templates/index', content=char)


@route('/static/<path:path>')
def callback(path):
    print os.path.abspath(os.path.split(sys.argv[0])[0]) + '/static'
    return static_file(path, root=os.path.abspath(os.path.split(sys.argv[0])[0])+'/static')


if __name__ == '__main__':
    run(host='0.0.0.0', port=7986)
