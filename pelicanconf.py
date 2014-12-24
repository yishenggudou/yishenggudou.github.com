#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

AUTHOR = u'timger'
SITENAME = u'马栏山下的程序员'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Dev', 'http://dev.timger.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = os.path.join(DIR_PATH, 'twenty-pelican-html5up')


def sidebar(value):
    if value.startswith('archives') or value.startswith('category'):
        return 'right-sidebar'
    elif value == 'index':
        return 'index'
    else:
        return 'no-sidebar'

JINJA_FILTERS = {'sidebar':sidebar}