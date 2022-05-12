# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""View method for Invenio-Formatter."""

from __future__ import absolute_import, print_function

import hashlib
from datetime import datetime as dt
from datetime import timedelta

from flask import Blueprint, Response, current_app, request


def create_badge_blueprint(allowed_types):
    """Create the badge blueprint.

    :param allowed_types: A list of allowed types.
    :returns: A Flask blueprint.
    """
    from invenio_formatter.context_processors.badges import (
        generate_badge_png,
        generate_badge_svg,
    )

    blueprint = Blueprint(
        "invenio_formatter_badges",
        __name__,
        template_folder="templates",
    )

    @blueprint.route(
        "/badge/<any({0}):title>/<path:value>.<any(svg, png):ext>".format(
            ", ".join(allowed_types)
        )
    )
    def badge(title, value, ext="svg"):
        """Generate a badge response."""
        if ext == "svg":
            generator = generate_badge_svg
            mimetype = "image/svg+xml"
        elif ext == "png":
            generator = generate_badge_png
            mimetype = "image/png"

        badge_title_mapping = current_app.config["FORMATTER_BADGES_TITLE_MAPPING"].get(
            title, title
        )
        response = Response(generator(badge_title_mapping, value), mimetype=mimetype)
        # Generate Etag from badge title and value.
        hashable_badge = "{0}.{1}".format(badge_title_mapping, value).encode("utf-8")
        response.set_etag(hashlib.sha1(hashable_badge).hexdigest())
        # Add headers to prevent caching.
        response.headers["Pragma"] = "no-cache"
        response.cache_control.no_cache = True
        response.cache_control.max_age = current_app.config[
            "FORMATTER_BADGES_MAX_CACHE_AGE"
        ]
        response.last_modified = dt.utcnow()
        extra = timedelta(seconds=current_app.config["FORMATTER_BADGES_MAX_CACHE_AGE"])
        response.expires = response.last_modified + extra
        return response.make_conditional(request)

    return blueprint
