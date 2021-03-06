#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'K\xf6rtner & Muth GmbH'
SITENAME = u'K\xf6rtner & Muth - LOCKBASE'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

THEME = "km-pelican-theme"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
PAGE_ORDER_BY = 'order'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
