from __future__ import absolute_import

from django.views.generic import ListView
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.utils.translation import ugettext as _

from tagtools.tagcloud import *
from tagtools.settings import *

from taggit.models import Tag, TaggedItem

def _get_queryset_and_model(queryset_or_model):
    """
    Given a ``QuerySet`` or a ``Model``, returns a two-tuple of
    (queryset, model).

    If a ``Model`` is given, the ``QuerySet`` returned will be created
    using its default manager.
    """
    try:
        return queryset_or_model, queryset_or_model.model
    except AttributeError:
        return queryset_or_model._default_manager.all(), queryset_or_model


class ListTaggedView(ListView):

    def get_queryset(self):
        try:
            queryset_or_model = self.kwargs.pop('queryset_or_model')
        except KeyError:
            raise AttributeError(_('tagged_object_list must be called with a queryset or a model.'))
        try:
            tag = self.kwargs.pop('tag')
        except KeyError:
            raise AttributeError(_('tagged_object_list must be called with a tag.'))
        try:
            self.tag_instance = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            raise Http404(_('No Tag found matching "%s".') % tag)
        _, model = _get_queryset_and_model(queryset_or_model)
        ct_model = ContentType.objects.get_for_model(model)
        ti_qs = TaggedItem.objects.filter(content_type=ct_model, tag=self.tag_instance)
        queryset = model.objects.filter(pk__in=[o.object_id for o in ti_qs])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListTaggedView, self).get_context_data(**kwargs)
        context['tag'] = self.tag_instance
        return context
tagged_object_list = ListTaggedView.as_view()
