# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Jinja utilities for Invenio applications.

Quick start
-----------
This section presents an example of the Invenio-Formatter features.
In this section we will create a simple page with a time formatter and a
`shields.io <http://shields.io>`_ badge.


First, let us create a new template page on which we will render some text,
and save it to some location (e.g.: ``/home/myuser/templates/index.html``)

.. code-block:: html

    {% set mydate = mydate|from_isodate -%}
    Today is {{ mydate.strftime('%Y-%m-%d') }}

    Your book: {{ badge_svg('isbn','9780399547331')|safe }}

Create a new Flask application and set some configuration for badge generation:

>>> from flask import Flask
>>> app = Flask('TestApp', template_folder='/home/myuser/templates')
>>> app.config.update(FORMATTER_BADGES_ALLOWED_TITLES=('isbn', 'ISBN', ))
>>> app.config.update(FORMATTER_BADGES_TITLE_MAPPING={'isbn': 'ISBN',})

.. note::

    By default the ``template_folder`` is the directory
    ``templates`` at the root of your flask application.

load the Invenio-Formatter extension and run the application:

>>> from invenio_formatter import InvenioFormatter
>>> ext_fmt = InvenioFormatter(app)
>>> app.run() # doctest: +SKIP

You should now be able to access the index page with formatted date and badge
examples at `http://localhost:5000 <http://localhost:5000>`_.

Badges endpoints
~~~~~~~~~~~~~~~~
In addition of generating an image of a shield badge, a badge-rendering
endpoint is also available for easy embedding on other websites.

You can modify the template as follows:

.. code-block:: html

    {% set mydate = mydate|from_isodate -%}
    Today is {{ mydate.strftime('%Y-%m-%d') }}

    Your book (with badge URL: ):
        <img src="{{ url_for('invenio_formatter_badges.badge',
         title='isbn', value='9780399547331', ext='svg') }}"></img>

Your badge will be visible on the page as before, and also directly accessible
at `http://localhost:5000/badge/ISBN/9780399547331.svg
<http://localhost:5000/badge/ISBN/9780399547331.svg>`_.
"""

from __future__ import absolute_import, print_function

from .ext import InvenioFormatter
from .version import __version__

__all__ = ('__version__', 'InvenioFormatter')
