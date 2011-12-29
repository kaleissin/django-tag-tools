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
        return _tag_app_map[app](model, steps, min_count)
    return ()

def _taggit_set_tags_for_model(tags, model):
    from taggit.models import Tag
    existing_tags = set(model.tags.all())
    current_tags = set()
    if not tags:
        model.tags.set()
    else:
        for tag in tags:
            t_obj, _ = Tag.objects.get_or_create(name=tag)
            current_tags.add(t_obj)
        if existing_tags != current_tags:
            model.tags.add(*tags)
            remove_tags = existing_tags - current_tags
            if remove_tags:
                model.tags.remove(*remove_tags)
    return model, existing_tags != current_tags

def _tagging_set_tags_for_model(tags, model):
    return model, None

def _generic_set_tags_for_model(tags, model):
    if getattr(model.tags, '__module__', False):
        return _taggit_set_tags_for_model(tags, model)
    return model, None

if TAG_APP == 'taggit':
    get_tagcloud_for_model = _taggit_cloud
    set_tags_for_model = _taggit_set_tags_for_model
elif TAG_APP == 'tagging':
    get_tagcloud_for_model = _tagging_cloud
    set_tags_for_model = _tagging_set_tags_for_model
else:
    get_tagcloud_for_model = _generic_get_tagcloud_for_model
    set_tags_for_model = _generic_set_tags_for_model
