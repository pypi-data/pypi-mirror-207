import collections

from django.utils.functional import cached_property
from wagtail.coreutils import resolve_model_string
from wagtail.blocks import BaseBlock

from .annotations import ContentAnnotations

__all__ = ['ContentProviderBlockMixin', 'Content', 'ContentContributorBlockMixin']


Content = collections.namedtuple('Content', field_names=['items', 'annotations'])


class ContentProviderBlockMixin(metaclass=BaseBlock):

    class Meta:
        target_model = None
        annotations = ContentAnnotations()
        content_class = Content

    @cached_property
    def model_class(self):
        return resolve_model_string(self.meta.target_model) # noqa

    def __init__(self, *args, target_model, **kwargs):

        super().__init__(*args, target_model=target_model, **kwargs)

    # noinspection PyMethodMayBeStatic
    def render_basic(self, value, context=None):
        return ''

    def create_content(self, **kwargs):
        return self.meta.content_class(**kwargs) # noqa

    # noinspection PyMethodMayBeStatic
    def derive_content(self, value, request=None):

        # request might be None when called from extract_references(), for example.

        return self.create_content(items=[], annotations=[])

    # noinspection PyMethodMayBeStatic
    def extract_references(self, value):
        return []

    # noinspection PyMethodMayBeStatic
    def clean_annotations(self, items, annotations=None):
        annotations = self.meta.annotations.clean(items, annotations) # noqa
        return annotations


class ContentContributorBlockMixin(metaclass=BaseBlock):

    class Meta:
        content_class = Content
        content_var = "content"
        items_and_annotations_var = "items_and_annotations"

    def create_content(self, **kwargs):
        return self.meta.content_class(**kwargs) # noqa

    # noinspection PyMethodMayBeStatic
    def contribute_content_to_context(self, value, content, context):

        if self.meta.content_var: # noqa
            context[self.meta.content_var] = list(zip(content.items, content.annotations)) if content.items else [] # noqa

        if self.meta.items_and_annotations_var: # noqa
            context[self.meta.items_and_annotations_var] = content.items, content.annotations # noqa
