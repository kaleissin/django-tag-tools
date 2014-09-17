from __future__ import unicode_literals

import unittest

from django import test as djangotest
from django.test.utils import override_settings

from tagtools.settings import _set_tag_app_order, _set_tag_app

class SetTagAppOrderTest(djangotest.TestCase):

    @override_settings(INSTALLED_APPS=('tagtools',))
    def test_set_tag_app_order_no_tag_apps(self):
        apps = _set_tag_app_order(('taggit', 'tagging'))
        self.assertEqual(apps, [])

    @override_settings(INSTALLED_APPS=('tagtools','taggit'))
    def test_set_tag_app_order_taggit(self):
        apps = _set_tag_app_order(('taggit', 'tagging'))
        self.assertEqual(apps, ['taggit'])

    @override_settings(INSTALLED_APPS=('tagtools','tagging'))
    def test_set_tag_app_order_tagging(self):
        apps = _set_tag_app_order(('taggit', 'tagging'))
        self.assertEqual(apps, ['tagging'])

    @override_settings(INSTALLED_APPS=('tagtools','taggit','tagging'))
    def test_set_tag_app_order_preferred_app1(self):
        apps = _set_tag_app_order(('taggit', 'tagging'))
        self.assertEqual(apps, ['taggit', 'tagging'])

    @override_settings(INSTALLED_APPS=('tagtools','taggit','tagging'))
    def test_set_tag_app_order_preferred_app2(self):
        apps = _set_tag_app_order(('tagging', 'taggit'))
        self.assertEqual(apps, ['tagging', 'taggit'])

    @override_settings(INSTALLED_APPS=('tagtools','tagging','taggit'))
    def test_set_tag_app_order_preferred_app3(self):
        apps = _set_tag_app_order(('taggit', 'tagging'))
        self.assertEqual(apps, ['taggit', 'tagging'])

    @override_settings(INSTALLED_APPS=('tagtools','tagging','taggit'))
    def test_set_tag_app_order_preferred_app4(self):
        apps = _set_tag_app_order(('tagging', 'taggit'))
        self.assertEqual(apps, ['tagging', 'taggit'])

class SetTagAppTest(unittest.TestCase):
    def test_set_tag_app_no_apps(self):
        self.assertEqual(None, _set_tag_app(None, []))
        self.assertEqual(None, _set_tag_app('foo', []))

    def test_set_tag_app_fallback(self):
        self.assertEqual('bar', _set_tag_app(None, ['bar']))
        self.assertEqual('bar', _set_tag_app('foo', ['bar']))

    def test_set_tag_app(self):
        self.assertEqual('foo', _set_tag_app('foo', ['bar', 'foo']))
        self.assertEqual('bar', _set_tag_app('bar', ['bar', 'foo']))

