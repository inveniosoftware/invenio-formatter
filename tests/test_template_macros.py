# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
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

"""Tests for Jinja2 filters."""

from __future__ import absolute_import, print_function

from datetime import date

from flask import render_template_string


def test_meta_twittercard(app):
    """Test macro meta_twittercard."""
    template = r"""
    {% from "invenio_formatter/macros/meta.html" import meta_twittercard %}
    {{meta_twittercard("TITLE", "DESC", card="CARD", site="SITE")}}
    """
    with app.test_request_context():
        html = render_template_string(template)
        assert '<meta name="twitter:card" content="CARD" />' in html
        assert '<meta name="twitter:site" content="SITE" />' in html
        assert '<meta name="twitter:title" content="TITLE" />' in html
        assert '<meta name="twitter:description" content="DESC" />' in html


def test_meta_opengraph(app):
    """Test macro meta_twittercard."""
    template = r"""
    {% from "invenio_formatter/macros/meta.html" import meta_opengraph %}
    {{meta_opengraph("TITLE", "DESC",
                     url="http://example.org", site_name="SITE")}}
    """
    with app.test_request_context():
        html = render_template_string(template)
        assert '<meta property="og:url" content="http://example.org" />' \
            in html
        assert '<meta property="og:site_name" content="SITE" />' in html
        assert '<meta property="og:title" content="TITLE" />' in html
        assert '<meta property="og:description" content="DESC" />' in html


def test_meta_highwire(app):
    """Test macro meta_twittercard."""
    template = r"""
    {% from "invenio_formatter/macros/meta.html" import meta_highwire %}
    {{meta_highwire(
        "TITLE", "DESC", authors=["Doe, John", "Smith, Joe"],
        publication_date=today)}}
    """
    with app.test_request_context():
        html = render_template_string(template, today=date(2002, 1, 1))
        assert '<meta name="citation_publication_date"' \
               ' content="2002/01/01" />' \
               in html
        assert '<meta name="citation_author"' \
               ' content="Doe, John" />' \
               in html
        assert '<meta name="citation_author"' \
               ' content="Smith, Joe" />' \
               in html


def test_meta_badges_formats_list(app):
    """Test macro badges_formats_list."""
    template = r"""
    {% from "invenio_formatter/macros/badges.html" import badges_formats_list
     %}
    {{ badges_formats_list('image.svg', 'link') }}
    """
    with app.test_request_context():
        html = render_template_string(template, today=date(2002, 1, 1))
        assert '<pre>&lt;a href="link"&gt;&lt;img src="image.svg"' in html
        assert '<pre>.. image:: image.svg' in html
        assert '<pre>[![DOI](image.svg)](link)' in html
