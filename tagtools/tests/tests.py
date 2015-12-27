from __future__ import unicode_literals

import unittest

from django.test import TestCase

import factory
from faker import Factory as Faker

from taggit.models import Tag

from tagtools.tools import get_tagcloud_for_model
from tagtools.tools import set_tags_for_model
from tagtools.tagcloud import BaseTagCloud

from tagtools.tests.models import Headline

fake = Faker.create()


class HeadlineFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Headline

    headline = factory.LazyAttribute(lambda t: fake.name())


class TagFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Tag

    name = factory.LazyAttribute(lambda t: fake.name())


class BaseTagCloudTest(unittest.TestCase):

    def test_empty_abstract_init(self):
        with self.assertRaises(NotImplementedError) as e:
            BaseTagCloud(None)
            self.assertEqual(e.exception, "This TagCloud has not been adapted to a model")


class TagCloudTestCase(TestCase):

    def setUp(self):
        self.headline1 = HeadlineFactory()
        self.headline2 = HeadlineFactory()
        self.headline3 = HeadlineFactory()
        self.tag1 = TagFactory()
        self.tag2 = TagFactory()
        self.tag3 = TagFactory()

    def test_get_tagcloud_for_model_empty(self):
        tagcloud = get_tagcloud_for_model(Headline)
        self.assertEqual(tagcloud, [])

    def test_get_tagcloud_for_model_one(self):
        self.headline1.tags.add(self.tag1)
        tagcloud = get_tagcloud_for_model(Headline)
        self.assertEqual(len(tagcloud), 1)
        self.assertEqual(tagcloud[0]['count'], 1)

    def test_get_tagcloud_for_model_several(self):
        self.headline1.tags.add(self.tag1)
        self.headline2.tags.add(self.tag1)
        self.headline3.tags.add(self.tag1)
        self.headline1.tags.add(self.tag2)
        self.headline2.tags.add(self.tag2)
        self.headline1.tags.add(self.tag3)
        tagcloud = get_tagcloud_for_model(Headline)
        self.assertEqual(len(tagcloud), 3)
        for item in tagcloud:
            if item['slug'] == self.tag1.slug:
                self.assertEqual(item['count'], 3)
            if item['slug'] == self.tag2.slug:
                self.assertEqual(item['count'], 2)
            if item['slug'] == self.tag3.slug:
                self.assertEqual(item['count'], 1)


class SetTagsTestCase(TestCase):

    def setUp(self):
        self.headline = HeadlineFactory()
        self.tags = ['tag1', 'tag2', 'tag3', 'tag4']
        for tag in self.tags:
            TagFactory(name=tag)

    def test_set_no_tag(self):
        obj, created = set_tags_for_model(None, self.headline)
        self.assertFalse(created)

    def test_set_one_tag(self):
        obj, created = set_tags_for_model(['tag1'], self.headline)
        self.assertTrue(created)

    def test_set_existing_tag(self):
        self.headline.tags.add(Tag.objects.get(name='tag1'))
        obj, created = set_tags_for_model(['tag1'], self.headline)
        self.assertFalse(created)

    def test_remove_existing_tag(self):
        self.headline.tags.add(Tag.objects.get(name='tag1'))
        obj, created = set_tags_for_model(None, self.headline)
        self.assertTrue(created)
