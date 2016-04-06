# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
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

"""Tests for template context processors."""

from __future__ import absolute_import, print_function


def test_views_badge_svg(app):
    """Test context processor badge generating a SVG."""
    with app.test_request_context():
        with app.test_client() as client:
            response = client.get('/badge/title/value.svg')
            response_data = response.get_data(as_text=True).replace(
                    '\n', '').replace(' ', '')
            assert 'fill-opacity=".3">title</text>' in response_data
            assert 'y="14">title</text>' in response_data
            assert 'fill-opacity=".3">value</text>' in response_data
            assert 'y="14">value</text>' in response_data


def test_views_badge_png(app):
    """Test context processor badge generating a SVG."""
    with app.test_request_context():
        with app.test_client() as client:
            response = client.get('/badge/title/value.png')
            assert b'\x89PNG\r\n' in response.data
