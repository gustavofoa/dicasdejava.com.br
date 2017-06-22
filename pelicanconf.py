#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gustavo Furtado de Oliveira Alves'
SITENAME = '{ Dicas de Java }'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 20

RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME']

# Enable i18n plugin.
# PLUGIN_PATHS = ['./pelican-plugins']
# PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']

# Theme
THEME = 'theme'

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'
