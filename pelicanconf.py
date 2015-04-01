#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'\u674e\u6797\u514b\u65af'
SITENAME = u'\u674e\u6797\u514b\u65af'
SITEURL = 'http://deanthompson.github.io'

TIMEZONE = 'Asia/Shanghai'
#TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'zh'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('Flask', 'http://flask.pocoo.org/'),
          ('Golang', 'http://golang.org'),)


# Social widget
SOCIAL = (#('Google+', 'https://plus.google.com/+YoungLeon/posts'),
        ('Stack Overflow', 'http://stackoverflow.com/users/1461780/leon-young'),
        ('Github', 'https://github.com/DeanThompson'),
        #('Twitter', 'https://twitter.com/compiletheory'),
        ('豆瓣', 'http://www.douban.com/people/Touchthesky/'),
        ('知乎', 'http://www.zhihu.com/people/leonyoung'),)

DEFAULT_PAGINATION = 5

# Date format
DATE_FORMAT = {
    'en': ('en_US','%a, %d %b %Y'),
    'zh': ('zh_CN','%Y-%m-%d(%a)'),
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = u"liyangliang"
GOOGLE_ANALYTICS = "UA-45384257-1"

GITHUB_URL = "https://github.com/DeanThompson"
TWITTER_USERNAME = "compiletheory"

# URL
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
AUTHOR_URL = 'author/{name}.html'
AUTHOR_SAVE_AS = 'author/{name}.html'
CATEGORY_URL = 'category/{name}.html'
CATEGORY_SAVE_AS = 'category/{name}.html'
TAG_URL = 'tag/{name}.html'
TAG_SAVE_AS = 'tag/{name}.html'
