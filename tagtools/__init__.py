from django.db.models.loading import cache as app_cache

from tagtools.tagcloud import *
from tagtools.settings import *

def _taggit_cloud(model, steps=CLOUD_STEPS, min_count=CLOUD_MIN_COUNT):
    cloud_calculator = TaggitCloud(model, steps, min_count)
    return cloud_calculator.calculate_cloud()

def _tagging_cloud(model, steps=CLOUD_STEPS, min_count=CLOUD_MIN_COUNT):
    try:
        from tagging.models import Tag
        return Tag.objects.cloud_for_model(model, steps=steps, min_count=min_count)
    except ImportError:
        return ()

_tag_app_map = {
    'taggit': _taggit_cloud,
    'tagging': _tagging_cloud,
}

def _generic_get_tagcloud_for_model(model, steps=CLOUD_STEPS, min_count=CLOUD_MIN_COUNT):
    for app in PREFERRED_APP_ORDER:
        if app_cache.get_app(app):
            return _tag_app_map[app](model, steps, min_count)
    return ()

if TAG_APP == 'taggit':
    get_tagcloud_for_model = _taggit_cloud
elif TAG_APP == 'tagging':
    get_tagcloud_for_model = _tagging_cloud
else:
    get_tagcloud_for_model = _generic_get_tagcloud_for_model
