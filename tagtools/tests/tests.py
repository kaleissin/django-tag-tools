from __future__ import unicode_literals

import unittest

from django.test import TestCase

import factory
from faker import Factory as Faker

from tagtools.tools import get_tagcloud_for_model
from tagtools.tagcloud import BaseTagCloud

from tagtools.tests.models import Headline

fake = Faker.create()


class HeadlineFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Headline

    headline = factory.LazyAttribute(lambda t: fake.name())
