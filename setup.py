#!/usr/bin/env python

from distutils.core import setup

setup(name='lawbreaker',
      version='2.3',
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
          'web': ["Flask",
                  "psycopg2-binary",
                  "requests",
                  "waitress",
              ]
          },
      include_package_data=True,
      )
