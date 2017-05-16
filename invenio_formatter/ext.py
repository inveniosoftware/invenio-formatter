# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
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

"""Jinja utilities for Invenio."""

from __future__ import absolute_import, print_function

from pkg_resources import DistributionNotFound, get_distribution

from . import config
from .filters.datetime import format_arrow, from_isodate, from_isodatetime, \
    to_arrow
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
        )

        if app.config['FORMATTER_BADGES_ENABLE']:
            from invenio_formatter.context_processors.badges import \
                badges_processor

            # Registration of context processors.
            app.context_processor(badges_processor)
            # Register blueprint.
            app.register_blueprint(create_badge_blueprint(
                app.config['FORMATTER_BADGES_ALLOWED_TITLES']))

        app.extensions['invenio-formatter'] = self

    @staticmethod
    def init_config(app):
        """Initialize configuration.

        .. note:: If CairoSVG is installed then the configuration
            ``FORMATTER_BADGES_ENABLE`` is ``True``.

        :param app: The Flask application.
        """
        try:
            get_distribution('CairoSVG')
            has_cairo = True
        except DistributionNotFound:
            has_cairo = False

        app.config.setdefault('FORMATTER_BADGES_ENABLE', has_cairo)

        for attr in dir(config):
            if attr.startswith('FORMATTER_'):
                app.config.setdefault(attr, getattr(config, attr))
