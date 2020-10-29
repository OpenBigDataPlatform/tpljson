# -*- coding: utf-8 -*-
"""
docs/conf.py - Configuration for Sphinx Documentation
see: https://www.sphinx-doc.org/en/master/usage/configuration.html
see: https://sphinx-rtd-theme.readthedocs.io/en/stable/
"""
from __future__ import unicode_literals

import os

import sphinx_rtd_theme as theme

PROJECT = 'tpljson'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.extlinks',
    'recommonmark',
    'sphinx_rtd_theme'
]
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}
master_doc = 'index'
project = PROJECT
year = '2020'
author = 'OpenBigDataProject'
copyright = '{}, {}'.format(year, author)
version = release = '0.1.0'

pygments_style = 'default'
templates_path = ['.']
extlinks = {
    'issue': ('https://github.com/OpenBigDataProject/{}/issues/%s'.format(project), '#'),
    'pr': ('https://github.com/OpenBigDataProject/{}/pull/%s'.format(project), 'PR #'),
}

html_theme = "sphinx_rtd_theme"
html_theme_path = [theme.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://github.com/OpenBigDataProject/{}/'.format(project)
}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False