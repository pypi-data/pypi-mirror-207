import os
import sys
import sphinx_rtd_theme
from recommonmark.transform import AutoStructify

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------
project = 'easierscrape'
copyright = '2023, Daniel Greco'
author = 'Daniel Greco'
release = '0.2.1'

master_doc = 'index'

# -- General configuration ---------------------------------------------------
extensions = ['recommonmark', 'sphinx.ext.autodoc', 'sphinx.ext.githubpages', 'sphinx.ext.napoleon']
source_suffix = ['.rst', '.md']

templates_path = []
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = []

def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)
