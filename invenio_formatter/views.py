# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""View method for Invenio-Formatter."""

from __future__ import absolute_import, print_function

from flask import Blueprint, Response, current_app


def create_badge_blueprint(allowed_types):
    """Create the badge blueprint.

    :param allowed_types: A list of allowed types.
    :returns: A Flask blueprint.
    """
    from invenio_formatter.context_processors.badges import \
        generate_badge_png, generate_badge_svg

    blueprint = Blueprint(
        'invenio_formatter_badges',
        __name__,
        template_folder='templates',
    )

    @blueprint.route(
        '/badge/<any({0}):title>/<path:value>.<any(svg, png):ext>'.format(
            ', '.join(allowed_types)))
    def badge(title, value, ext='svg'):
        """Generate a badge response."""
        if ext == 'svg':
            generator = generate_badge_svg
            mimetype = 'image/svg+xml'
        elif ext == 'png':
            generator = generate_badge_png
            mimetype = 'image/png'
        return Response(
            generator(
                current_app.config['FORMATTER_BADGES_TITLE_MAPPING'].get(
                    title, title),
                value),
            mimetype=mimetype)

    return blueprint
