# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask
from mock import patch
from pkg_resources import DistributionNotFound

from invenio_formatter import InvenioFormatter


def test_version():
    """Test version import."""
    from invenio_formatter import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioFormatter(app)
    assert "invenio-formatter" in app.extensions

    app = Flask("testapp")
    ext = InvenioFormatter()
    assert "invenio-formatter" not in app.extensions
    ext.init_app(app)
    assert "invenio-formatter" in app.extensions


def test_badge_enable_disable():
    """Test if badge is disabled if CairoSVG is not installed."""
    app = Flask("testapp")
    InvenioFormatter(app)
    assert app.config["FORMATTER_BADGES_ENABLE"] is True
    assert "invenio_formatter_badges" in app.blueprints

    with patch("invenio_formatter.ext.get_distribution") as f:
        f.side_effect = DistributionNotFound

        app = Flask("testapp")
        InvenioFormatter(app)
        assert app.config["FORMATTER_BADGES_ENABLE"] is False
        assert "invenio_formatter_badges" not in app.blueprints
