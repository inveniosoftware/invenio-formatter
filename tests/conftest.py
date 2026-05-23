# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT


"""Pytest configuration."""

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
