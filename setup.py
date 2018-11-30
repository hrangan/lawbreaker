#!/usr/bin/env python

from distutils.core import setup

setup(name='lawbreaker',
      version='2.0',
      description='A character generator for Knave',
      author='Harshavardhan Rangan',
      author_email='hvardhan.r@gmail.com',
      packages=['lawbreaker'],
      entry_points={
          'console_scripts': [
              'knave = lawbreaker.knave:main',
             ],
            }
      )
