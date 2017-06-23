#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gustavo Furtado de Oliveira Alves'
SITENAME = '{ Dicas de Java }'
SITEURL = 'http://dicasdejava.com.br'
CONTACT_EMAIL = 'gustavo@dicasdeprogramacao.com.br'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_DATE_FORMAT = '%d de %B de %Y'

DEFAULT_LANG = u'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME', 'images']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap']

# Theme
THEME = 'theme'
DISPLAY_CATEGORIES_ON_MENU = True;

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

#Config slugs
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'autor/{slug}/'
AUTHOR_SAVE_AS = 'autor/{slug}/index.html'
CATEGORY_URL = 'categoria/{slug}/'
CATEGORY_SAVE_AS = 'categoria/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_URL = 'arquivo/'
ARCHIVES_SAVE_AS = 'arquivo/index.html'

# PAGINATED_DIRECT_TEMPLATES = ['archives']
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
DEFAULT_PAGINATION = 20
SUMMARY_MAX_LENGTH = 20

AUTHORS = {
    'Gustavo Furtado de Oliveira Alves': {
        'summary':'É mestre em computação aplicada pelo Institudo Nacional de Pesquisas Espaciais, '+
                  'Engenheiro da Computação pela ETEP Faculdades e '+
                  'Técnico em Informática pela Escola Técnica Pandiá Calógeras. '+
                  'Possui as certificações SCJP, SCWCD e ASF e trabalha com desenvolvimento de softwares desde 2007.',
        'image': '/images/author-gustavo.jpeg'
    }
}

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
