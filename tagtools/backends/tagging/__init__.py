from __future__ import absolute_import

from tagtools.tagcloud import *
from tagtools.settings import *
from tagging.models import Tag

def get_tagcloud_for_model(model, steps=CLOUD_STEPS, min_count=CLOUD_MIN_COUNT):
    return Tag.objects.cloud_for_model(model, steps=steps, min_count=min_count)

def set_tags_for_model(tags, model):
    return model, None
