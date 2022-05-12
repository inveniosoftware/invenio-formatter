# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Pytest configuration."""

from __future__ import absolute_import, print_function

import pytest
from flask import Flask
from invenio_i18n import InvenioI18N

from invenio_formatter import InvenioFormatter


@pytest.fixture()
def app():
    """Flask application fixture."""
    app = Flask("testapp")
    app.config.update(
        TESTING=True,
        ALLOWED_HTML_TAGS=[
            "a",
        ],
        ALLOWED_HTML_ATTRS={
            "a": ["href"],
        },
    )
    InvenioI18N(app)
    InvenioFormatter(app)
    return app
