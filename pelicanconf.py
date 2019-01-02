#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from functools import partial

# Basic settings
AUTHOR = 'Daniel Pye'
SITENAME = 'Daniel Pye'
SITEURL = ''
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'
MARKUP = ('md', 'ipynb')

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['materialbox.materialbox', 'ipynb2pelican']
IGNORE_FILES = [".ipynb_checkpoints"]

# Paths
PATH = 'content'
THEME = 'theme'
IMAGES_DIR = 'images'
STATIC_PATHS = ['images', 'pages']
STATIC_EXCLUDES = []

# Menu settings
MENUITEMS = (
            ('Home','/'),
            ('Articles','/articles/'),
            )
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Blog settings
DEFAULT_PAGINATION = 8
NEWEST_FIRST_ARCHIVES = True
IPYNB_USE_METACELL = True

# Misc variables
SUBHEADING = 'Digitally Enhanced Investigations'

# Jinja settings
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order

# Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Build only modified content
LOAD_CONTENT_CACHE = False
CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
