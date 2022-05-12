# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Jinja utilities for Invenio."""

from __future__ import absolute_import, print_function

from pkg_resources import DistributionNotFound, get_distribution

from . import config
from .filters.datetime import format_arrow, from_isodate, from_isodatetime, to_arrow
from .filters.html import sanitize_html
from .views import create_badge_blueprint


class InvenioFormatter(object):
    """Invenio-Formatter extension."""

    def __init__(self, app=None):
        """Extension initialization.

        :param app: The Flask application. (Default: ``None``)
        """
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization.

        :param app: The Flask application.
        """
        self.init_config(app)

        # Install datetime helpers.
        app.jinja_env.filters.update(
            from_isodate=from_isodate,
            from_isodatetime=from_isodatetime,
            to_arrow=to_arrow,
            format_arrow=format_arrow,
            sanitize_html=sanitize_html,
        )

        if app.config["FORMATTER_BADGES_ENABLE"]:
            from invenio_formatter.context_processors.badges import badges_processor

            # Registration of context processors.
            app.context_processor(badges_processor)
            # Register blueprint.
            app.register_blueprint(
                create_badge_blueprint(app.config["FORMATTER_BADGES_ALLOWED_TITLES"])
            )

        app.extensions["invenio-formatter"] = self

    @staticmethod
    def init_config(app):
        """Initialize configuration.

        .. note:: If CairoSVG is installed then the configuration
            ``FORMATTER_BADGES_ENABLE`` is ``True``.

        :param app: The Flask application.
        """
        try:
            get_distribution("CairoSVG")
            has_cairo = True
        except DistributionNotFound:
            has_cairo = False

        app.config.setdefault("FORMATTER_BADGES_ENABLE", has_cairo)

        for attr in dir(config):
            if attr.startswith("FORMATTER_"):
                app.config.setdefault(attr, getattr(config, attr))
