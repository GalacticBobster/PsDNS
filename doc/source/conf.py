# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, '..')


# -- Project information -----------------------------------------------------

project = 'PsDNS'
copyright = '2020, 2021'
author = 'Daniel M. Israel'
version = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'matplotlib.sphinxext.plot_directive',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

numfig = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_theme_options = {
    'show_relbars': True
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []


# -- Extension configuration -------------------------------------------------

# -- Options for autodoc extension -------------------------------------------

autoclass_content = 'both'
autodoc_default_options = {
    'inherited-members': False,
    'member-order': 'bysource',
    }
autodoc_inherit_docstrings = False

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    }

plot_html_show_formats = False
plot_html_show_source_link = False
plot_pre_code = \
r"""import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np 

fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
   
plt.tight_layout()

ax.xaxis.set_pane_color((0,0,0,0))
ax.yaxis.set_pane_color((0,0,0,0))
ax.zaxis.set_pane_color((0,0,0,0))
ax.xaxis.line.set_color((0,0,0,0))
ax.yaxis.line.set_color((0,0,0,0))
ax.zaxis.line.set_color((0,0,0,0))
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.xaxis.labelpad = -16
ax.yaxis.labelpad = -16
ax.zaxis.labelpad = -16
ax.grid(False)
"""

def cut_pep257_summary(app, what, name, obj, options, lines):
    """Remove summary lines from PEP 257 formatted docstrings.

    According to :pep:`257`, multi-line docstrings should consist of a
    one line summary, followed by a blank line, followed by the more
    detailed documentation.  This processor checks for docstrings that
    appear to be in that format, and removes the summary line.

    The rationale is that summary lines are typically useful as
    headers when using the Python :func:`help` function, but are
    redundant in the printed documentation where sections have titles
    or headers.
    """
    if len(lines) > 2 and lines[1] == "":
        del lines[:2]


def setup(app):
    app.connect('autodoc-process-docstring', cut_pep257_summary)
