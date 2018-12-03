#!/usr/bin/env python

from distutils.core import setup

setup(name='lawbreaker',
      version='2.1',
      description='A character generator for Knave',
      author='Harshavardhan Rangan',
      author_email='hvardhan.r@gmail.com',
      packages=['lawbreaker',
                'lawbreaker.web',
                ],
      entry_points={
          'console_scripts': [
              'knave = lawbreaker.knave:main',
              'knave.web = lawbreaker.web.server:main[web]',
             ],
            },
      extras_require={
          'web': ["Flask==1.0.2",
                  "psycopg2-binary==2.7.6.1",
                  "requests==2.20.1",
                  "waitress==1.1.0",
              ]
          },
      include_package_data=True,
      )
