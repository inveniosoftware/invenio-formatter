# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for template context processors."""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_formatter import InvenioFormatter


def test_views_badge_svg(app):
    """Test context processor badge generating a SVG."""
    with app.app_context():
        with app.test_client() as client:
            response = client.get("/badge/DOI/value.svg")
            response_data = (
                response.get_data(as_text=True).replace("\n", "").replace(" ", "")
            )
            assert 'fill-opacity=".3">DOI</text>' in response_data
            assert 'y="14">DOI</text>' in response_data
            assert 'fill-opacity=".3">value</text>' in response_data
            assert 'y="14">value</text>' in response_data

            # Unallowed title
            assert client.get("/badge/invalid/value.svg").status_code == 404


def test_views_badge_svg_mapping():
    """Test context processor badge generating a SVG."""
    """Flask application fixture."""
    app = Flask("testapp")
    app.config.update(
        TESTING=True,
        FORMATTER_BADGES_ALLOWED_TITLES=["test", "TEST"],
        FORMATTER_BADGES_TITLE_MAPPING={"test": "TEST"},
    )
    InvenioFormatter(app)

    with app.app_context():
        with app.test_client() as client:
            response = client.get("/badge/test/value.svg")
            response_data = (
                response.get_data(as_text=True).replace("\n", "").replace(" ", "")
            )
            assert 'fill-opacity=".3">TEST</text>' in response_data

            response = client.get("/badge/TEST/value.svg")
            response_data = (
                response.get_data(as_text=True).replace("\n", "").replace(" ", "")
            )
            assert 'fill-opacity=".3">TEST</text>' in response_data


def test_views_badge_png(app):
    """Test context processor badge generating a SVG."""
    with app.app_context():
        with app.test_client() as client:
            response = client.get("/badge/DOI/value.png")
            assert b"\x89PNG\r\n" in response.data


def test_views_badge_etag(app):
    """Test Etag for badges."""
    with app.app_context():
        with app.test_client() as client:
            response = client.get("/badge/DOI/value.png")
            response = client.get(
                "/badge/DOI/value.png",
                headers={"If-None-Match": response.headers["ETag"]},
            )
            assert response.status_code == 304


def test_views_badge_no_cache_headers(app):
    """Test Etag for badges."""
    with app.app_context():
        with app.test_client() as client:
            response = client.get("/badge/DOI/value.png")
            assert response.headers["Pragma"] == "no-cache"
            cache_control_values = ["no-cache", "max-age"]
            assert set(cache_control_values).issubset(response.cache_control)
            assert response.last_modified
            assert response.expires
            assert response.get_etag()[0]
