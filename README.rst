=========
Tag tools
=========

This currently provides a tag cloud generator for django-taggit.

Optional settings
-----------------

TAGTOOLS_CLOUD_STEPS
    How many different sizes of tags for the cloud. **Default:** 6

TAGTOOLS_CLOUD_MIN_COUNT
    Minimum frequency of a tag before it is included. **Default:** 1

Usage
-----

There's a view ``tagged_object_list`` if you want to devote an entire
page to a tag-cloud. In your url-conf:

    tags_dict= {
            'queryset_or_model': YourTaggedModel,
            'template_name': 'sometemplate.html',
            }

    urlpatterns = patterns('tagtools.views',
        (r'^tag/(?P<tag>[-\w\d]+)/$', 'tagged_object_list', tags_dict),
    )

You can generate lists of tags in a view with the function
``tagtools.get_tagcloud_for_model``.

You can set tags for a model with ``tagtools.set_tags_for_model``.


:Version: 0.2.0
