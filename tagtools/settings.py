# coding: utf-8

from __future__ import absolute_import, unicode_literals

from django.conf import settings
_DEFAULT_CLOUD_STEPS = 6
_DEFAULT_CLOUD_MIN_COUNT = 1

CLOUD_STEPS = getattr(settings, 'TAGTOOLS_CLOUD_STEPS', _DEFAULT_CLOUD_STEPS)
CLOUD_MIN_COUNT = getattr(settings, 'TAGTOOLS_CLOUD_MIN_COUNT', _DEFAULT_CLOUD_MIN_COUNT)
