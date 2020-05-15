#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cong Lin'
SITENAME = u"Cong Lin's Ideas Repo"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME="/Users/user/projects/twenty-pelican-html5up"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['/Users/user/Documents/projects/pelican-plugins']
PLUGINS = ['i18n_subsites']
I18N_TEMPLATES_LANG = 'zh'
BOOTSTRAP_FLUID = True
from filters import sidebar
JINJA_FILTERS = {"sidebar": sidebar}