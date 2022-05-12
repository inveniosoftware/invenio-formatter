# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for template context processors."""

from __future__ import absolute_import, print_function

from flask import render_template_string


def test_context_processor_badge_svg(app):
    """Test context processor badge generating a SVG."""
    template = r"""
    {{ badge_svg('DOI','10.1234/zenodo.12345')|safe }}
    """
    with app.test_request_context():
        html = render_template_string(template)
        html = html.replace("\n", "").replace(" ", "")
        assert 'fill-opacity=".3">DOI</text>' in html
        assert 'y="14">DOI</text>' in html
        assert 'fill-opacity=".3">10.1234/zenodo.12345</text>' in html
        assert 'y="14">10.1234/zenodo.12345</text>' in html


def test_context_processor_badge_png(app):
    """Test context processor badge generating a PNG."""
    template = r"""
    {{ badge_png('this_is_the_title','this_is_the_value') }}
    """
    with app.test_request_context():
        html = render_template_string(template)
        assert "data:image/png;base64," in html
