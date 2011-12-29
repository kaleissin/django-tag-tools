
# -*- coding: utf8 -*-

import math
import logging
_LOG = logging.getLogger(__name__)

from django.contrib.contenttypes.models import ContentType
from django.db.models import Count, Max, Min

class BaseTagCloud(object):
    """
    Calculates a django-tagging-style tag-cloud.

    Adapt set_tags() to a suitable tagging-module.
    """

    def __init__(self, model, steps=6, min_count=1, alphabetic=True):
        self.steps = steps
        self.min_count = min_count
        self.model = model
        self.alphabetic = True
        self.set_tags()
        self.find_min_max()
        self.thresholds = self.calculate_thresholds()

    def set_tags(self):
        """
        Adapted to django-taggit
        """
        raise NotImplementedError, "This TagCloud has not been adapted to a model"

    def find_min_max(self):
        edges = self.queryset.aggregate(max=Max('count'), min=Min('count'))
        self.max_weight = edges['max']
        self.min_weight = edges['min']

    def calculate_thresholds(self):
        delta = (self.max_weight - self.min_weight) / float(self.steps)
        return [self.min_weight + i * delta for i in range(1, self.steps + 1)]

    def calculate_tag_weight(self, weight):
        """
        Logarithmic tag weight calculation is based on code from the
        `Tag Cloud`_ plugin for Mephisto, by Sven Fuchs.

        .. _`Tag Cloud`: http://www.artweb-design.de/projects/mephisto-plugin-tag-cloud
        """
        if self.max_weight == 1:
            return weight
        else:
            # Fuchs-method
            return math.log(weight) * self.max_weight / math.log(self.max_weight)

    def calculate_cloud(self):
        """
        Add a ``font_size`` attribute to each tag according to the
        frequency of its use, as indicated by its ``count``
        attribute.

        ``steps`` defines the range of font sizes - ``font_size`` will
        be an integer between 1 and ``steps`` (inclusive).
        """
        tags = []
        if len(self.tags):
            for tag in self.tags:
                font_set = False
                tag_weight = self.calculate_tag_weight(tag['count'])
                for i in range(self.steps):
                    if not font_set and tag_weight <= self.thresholds[i]:
                        tag['font_size'] = i + 1
                        font_set = True
                tags.append(tag)
        return tags

class TaggitCloud(BaseTagCloud):
    """
    Given a model with django-taggit's TaggableManager, calculates a
    django-tagging-style tag-cloud.
    """

    def set_tags(self):
        """
        Adapted to django-taggit
        """
        from taggit.models import Tag, TaggedItem
        ct = ContentType.objects.get_for_model(self.model)
        tagitems = TaggedItem.objects.filter(content_type=ct).values_list('tag_id',
                flat=True)
        queryset = Tag.objects.filter(id__in=tagitems)
        queryset = queryset.annotate(count=Count('taggit_taggeditem_items'))
        queryset = queryset.filter(count__gte=self.min_count)
        if self.alphabetic:
            queryset = queryset.order_by('name')
        self.queryset = queryset
        self.tags = self.queryset.values('name', 'slug', 'count')
