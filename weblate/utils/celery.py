# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2018 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""Whoosh based full text search."""

from __future__ import absolute_import, unicode_literals

from weblate.celery import app as celery_app


def extract_batch_args(*args):
    """
    Wrapper to extract args from batch task.

    It can be either passed directly in eager mode or as requests in
    batch mode.
    """
    if isinstance(args[0], list):
        return [args]
    return [request.args for request in args]


def get_queue_length():
    with celery_app.connection_or_acquire() as conn:
        return conn.default_channel.queue_declare(queue='celery').message_count