#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.timger.info'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = "feeds/%s.tag.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "yishenggudou"
GOOGLE_ANALYTICS = "UA-29124639-1"



AUTHOR = u'@timger'
SITENAME = u'@timger'
SITEURL = 'http://www.timger.info'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
          ('Pelican', 'http://getpelican.com/'),
          )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
DATE_FORMATS = {
    'en':('usa','%a, %d %b %Y'),
    'zh':('chs','%Y-%m-%d, %a'),
    'jp':('jpn','%Y/%m/%d (%a)'),
}
# windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
LOCALE = ['usa', 'chs', 'jpn',        # windows
          'en_US', 'zh_CN', 'ja_JP']  # Unix/Linux
DEFAULT_LANG = 'zh'

AUTHOR = 'timger'

DISQUS_SITENAME = 'yishenggudou'
GITHUB_URL = 'https://github.com/yishenggudou'
SITEURL = 'http://yishenggudou.github.com'

SOCIAL = (('twitter', 'http://twitter.com/yishenggudou'),
          ('github', 'https://github.com/yishenggudou'),
          ('facebook', 'http://www.facebook.com/yishenggudou'),
          ('weibo', 'http://weibo.com/zhanghaibo'),
          ('renren', 'http://www.renren.com/zhanghaibo'),
          )


TWITTER_USERNAME = 'yishenggudou'

THEME = "/Library/Python/2.7/site-packages/pelican/themes/zurb-F5-basic"

#CSS_FILE = "wide.css"

DEFAULT_CATEGORY ='Others'


FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }


# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
