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

# Default theme language.
TIMEZONE = 'America/Sao_Paulo'
I18N_TEMPLATES_LANG = 'pt_BR'
# Your language.
DEFAULT_LANG = 'pt_BR'
OG_LOCALE = 'pt_BR'
LOCALE = ('pt','bra', 'pt_BR')
LANGUAGE = 'pt_BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True

STATIC_PATHS = ['pages/extra/CNAME', 'images', 'pages/extra/custom.css', 'admin']

TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}

EXTRA_PATH_METADATA = {
    'pages/extra/CNAME': {'path': 'CNAME'},
	'pages/extra/custom.css': {'path': 'custom.css'}
}

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['tag_cloud']

# MD_EXTENSIONS = ['codehilite', 'extra']

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
DEFAULT_PAGINATION = 12
SUMMARY_MAX_LENGTH = 30

DEFAULT_ADSENSE = {
	'adClientId' : 'ca-pub-6041601556788047',
	'adSlot' : {
		'top_responsible' : '9578335779',
		'rside_300x600' : '3531802173',
		'bottom_responsible' : '7962001772'
	}
}

DEFAULT_HOTMART = 'banners/gustavo/banner-hotmart.html'

AUTHORS = {
    'Gustavo Furtado de Oliveira Alves': {
        'summary': 'É mestre em computação aplicada pelo Institudo Nacional de Pesquisas Espaciais, '+
                  'Engenheiro da Computação pela ETEP Faculdades e '+
                  'Técnico em Informática pela Escola Técnica Pandiá Calógeras. '+
                  'Possui as certificações SCJP-6, SCWCD-5 e ASF '+
                  'e trabalha com desenvolvimento de softwares desde 2007.',
        'image': 'https://dicasdejava.com.br/images/author-gustavo.jpeg',
        'adsense': DEFAULT_ADSENSE,
        'hotmart': DEFAULT_HOTMART
    },
	'Pedro Henrique Ribeiro Rodrigues': {
		'summary': 'Desenvolvedor Java desde 2008, fullstack desde 2012, geek e gamer desde sempre.',
		'image': 'https://media.licdn.com/mpr/mpr/shrinknp_400_400/AAEAAQAAAAAAAAtTAAAAJDQzNTY1YThkLWYyNGYtNGI0My1hYzE2LTkzNDI5NmQwOGE2ZA.jpg',
		'adsense': {
			'adClientId' : 'ca-pub-3499823579380102',
			'adSlot' : {
				'top_responsible' : '4001442477',
				'rside_300x600' : '8431642073',
				'bottom_responsible' : '4001442477'
			}
		},
    'hotmart': 'banners/pedro/banner-hotmart.html'
	}
}
