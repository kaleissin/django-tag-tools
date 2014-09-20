from __future__ import absolute_import

from tagtools.tagcloud import *
from tagtools.settings import *
from taggit.models import Tag

def get_tagcloud_for_model(model, steps=CLOUD_STEPS, min_count=CLOUD_MIN_COUNT):
    cloud_calculator = TaggitCloud(model, steps, min_count)
    return cloud_calculator.calculate_cloud()

def set_tags_for_model(tags, model):
    existing_tags = set(model.tags.all())
    current_tags = set()
    if not tags:
        model.tags.set()
    else:
        for tag in tags:
            t_obj, created = Tag.objects.get_or_create(name=tag)
            if created:
                # Make sure the slug is generated
                t_obj.save()
            current_tags.add(t_obj)
        if existing_tags != current_tags:
            model.tags.add(*tags)
            remove_tags = existing_tags - current_tags
            if remove_tags:
                model.tags.remove(*remove_tags)
    return model, existing_tags != current_tags
