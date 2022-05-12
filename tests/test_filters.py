# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for Jinja2 filters."""

from __future__ import absolute_import, print_function

from datetime import date, datetime

import arrow
import pytest
from arrow.parser import ParserError
from flask import render_template_string


def test_from_isodate(app):
    """Test from_isodate filter."""
    with app.test_request_context():
        assert (
            render_template_string(
                "{{ 'yes' if dt|from_isodate < now else 'no'}}",
                dt="2002-01-01",
                now=date.today(),
            )
            == "yes"
        )
        assert render_template_string("{{ dt|from_isodate }}", dt="") == "None"
        assert (
            render_template_string(
                "{{ dt|from_isodate }}", dt=datetime(2002, 1, 1, 1, 1)
            )
            == "2002-01-01"
        )
        pytest.raises(
            TypeError,
            render_template_string,
            "{{ 'yes' if dt < now else 'no'}}",
            dt="2002-01-01",
            now=date.today(),
        )
        pytest.raises(
            ParserError,
            render_template_string,
            "{{ dt|from_isodate }}",
            dt="abcd-01-01",
        )
        pytest.raises(
            ParserError,
            render_template_string,
            "{{ dt|from_isodate(strict=True) }}",
            dt="",
        )

        # Test pre-1900 centuries.
        assert (
            render_template_string(
                "{{ '0001-01-01'|from_isodate > '1500-01-01'|from_isodate }}"
            )
            == "False"
        )


def test_from_isodatetime(app):
    """Test from_isodate filter."""
    with app.test_request_context():
        assert (
            render_template_string(
                "{{ 'yes' if dt|from_isodatetime < now else 'no'}}",
                dt="2002-01-01T00:01:00",
                now=arrow.now(),
            )
            == "yes"
        )

        assert render_template_string("{{ dt|from_isodatetime }}", dt="") == "None"
        assert (
            render_template_string(
                "{{ dt|from_isodatetime }}", dt=datetime(2002, 1, 1, 1, 1)
            )
            == "2002-01-01 01:01:00+00:00"
        )
        pytest.raises(
            TypeError,
            render_template_string,
            "{{ 'yes' if dt < now else 'no'}}",
            dt="2002-01-01T00:01",
            now=arrow.now(),
        )
        pytest.raises(
            ParserError,
            render_template_string,
            "{{ dt|from_isodatetime }}",
            dt="abcd-01-01T00:00:00",
        )
        pytest.raises(
            ParserError,
            render_template_string,
            "{{ dt|from_isodatetime(strict=True) }}",
            dt="",
        )

        # Test pre-1900 centuries.
        assert (
            render_template_string(
                "{{ '0001-01-01T00:00:00'|from_isodatetime"
                " > '1500-01-01'|from_isodatetime }}"
            )
            == "False"
        )


@pytest.mark.parametrize(
    "malicious_html,sanitized_html",
    [
        (
            '<a href="data:text/html;base64,'
            'PHNjcmlwdD5hbGVydChkb2N1bWVudC5kb21haW4pPC9zY3JpcHQ+Cg==">XSS</a>',
            "&lt;a&gt;XSS&lt;/a&gt;",
        ),
        ("<svg/onload=alert(document.origin)>", ""),
        ("<img src='x' onerror='alert(document.domain)' />", ""),
    ],
)
def test_sanitize_html(app, malicious_html, sanitized_html):
    """Test from_isodate filter."""
    with app.test_request_context():
        assert (
            render_template_string(
                "{{ content | sanitize_html() }}", content=malicious_html
            )
            == sanitized_html
        )
