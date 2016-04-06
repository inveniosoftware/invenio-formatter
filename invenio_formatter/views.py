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

"""View method for Invenio-Formatter."""

from __future__ import absolute_import, print_function

from flask import Blueprint, Response

from .context_processors.badges import generate_badge_png, generate_badge_svg

blueprint = Blueprint(
    'invenio_formatter',
    __name__,
    template_folder='templates',
)


@blueprint.route('/badge/<title>/<path:value>.svg')
def badge_svg(title, value):
    """Generate a SVG badge response."""
    return Response(generate_badge_svg(title, value),
                    mimetype='image/svg+xml')


@blueprint.route('/badge/<title>/<path:value>.png')
def badge_png(title, value):
    """Generate a PNG badge response."""
    return Response(generate_badge_png(title, value),
                    mimetype='image/png')
