#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vigil Varghese'
SITENAME = u"Vigil's Corner!"
SITEURL = u'http://vigilv.com'

PATH = 'content'
OUTPUT_PATH = 'output/'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Uncoment when using plugins
# PLUGIN_PATH = '../pelican-plugins'
# PLUGINS = ['a-plugin']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# clean urls for pages, trailing slash to support HTTPS
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# clean urls for articles
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'

DEFAULT_PAGINATION = 10

THEME = '../themes/pelican-elegant'
PLUGIN_PATHS=['../pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'post_stats']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
     },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
