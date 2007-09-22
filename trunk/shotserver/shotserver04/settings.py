# -*- coding: utf-8 -*-
# browsershots.org - Test your web design in different browsers
# Copyright (C) 2007 Johann C. Rocholl <johann@browsershots.org>
#
# Browsershots is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Browsershots is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Django configuration for the ShotServer.
"""

__revision__ = "$Rev$"
__date__ = "$Date$"
__author__ = "$Author$"

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Johann C. Rocholl', 'johann@browsershots.org'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql' # 'postgresql', 'mysql', 'sqlite3', 'ado_mssql'.
DATABASE_NAME = 'shotserver04' # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost.
DATABASE_PORT = ''             # Set to empty string for default.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Don't append slash to URLs because of
# http://browsershots.org/http://www.example.com/no-slash
APPEND_SLASH = False

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    #('bg', u'Български'),
    ('cs', u'Česky'),
    ('da', u'Dansk'),
    ('de', u'Deutsch'),
    ('en', u'English'),
    #('es', u'Español'),
    ('fr', u'Français'),
    #('it', u'Italiano'),
    #('lt', u'Lietuviškai'),
    ('nl', u'Nederlands'),
    ('pl', u'Polski'),
    ('pt-br', u'Português'),
    #('ru', u'Русский'),
    ('sv', u'Svenska'),
    #('tr', u'Türkçe'),
    #('zh-tw', u'中文'),
    )

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

PNG_ROOT = '/var/www/v04.browsershots.org/png/'
PNG_URL = 'http://png.browsershots.org/'

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    #'django.core.context_processors.request',
    'shotserver04.common.context_processors.http_request',
    )

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Profanity filter
PROFANITIES_LIST = """
asshat asshead asshole cunt fuck gook nigger shit
porn p0rn pr0n boys girls chicks babe cock bukkake
sex xxx nude nudist naked bitcafe stile omglol
""".lower().split()

# Tolerate a small number of profane words
PROFANITIES_ALLOWED = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y7v!*06i+q2e!4zqwr_wnc=#lnm*ew&!1o_z-cki^^*4*ww=16'

# Account number for Google Analytics, e.g. UA-123456-7
GOOGLE_ANALYTICS_ACCOUNT = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    # 'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'shotserver04.common.middleware.RedirectMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'shotserver04.urls'

# Dynamic path trickery
import os
SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))

# Find templates next to settings.py
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'shotserver04.start',
    'shotserver04.accounts',
    'shotserver04.common',
    'shotserver04.platforms',
    'shotserver04.sponsors',
    'shotserver04.factories',
    'shotserver04.features',
    'shotserver04.browsers',
    'shotserver04.websites',
    'shotserver04.requests',
    'shotserver04.screenshots',
    'shotserver04.nonces',
    'shotserver04.xmlrpc',
    'shotserver04.redirect',
    'shotserver04.messages',
    'shotserver04.status',
)

# Override secret settings from secrets.py,
# if that file exists in the same folder as settings.py.
try:
    from secrets import *
except ImportError:
    pass
if 'EXTRA_APPS' in locals():
    INSTALLED_APPS += EXTRA_APPS