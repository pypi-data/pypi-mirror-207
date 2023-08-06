import json

from django.utils.deconstruct import deconstructible
from django.utils.functional import cached_property

# from wagtail.blocks import PageChooserBlock
from wagtail.admin.widgets.chooser import AdminPageChooser
from wagtail.telepath import JSContext

from .dotted_paths import parse_dotted_path_components, value_at_dotted_path

__all__ = ['ContentAnnotations',
           'ContentAnnotationGroup',
           'ContentAnnotationField',
           'TextAreaAnnotationField',
           'TextAnnotationField',
           'NumberAnnotationField',
           'RadioButtonAnnotationField',
           'CheckboxAnnotationField',
           'ChoiceAnnotationField',
           'PageChooserAnnotationField']


@deconstructible
class BaseDescriptor:

    @property
    def identifier(self):
        return self._identifier

    @property
    def label(self):
        return self._label

    def __init__(self, *, identifier, label, **kwargs):

        self._identifier = identifier
        self._label = label

    def pack(self):
        return {"identifier": self.identifier, "label": self.label}


class ContentAnnotationField(BaseDescriptor):

    @property
    def type(self):
        return self._type

    @property
    def default_value(self):
        return self._default_value

    @cached_property
    def instance_value_path(self):
        return self._instance_value_path

    @cached_property
    def instance_value_path_components(self):
        return parse_dotted_path_components(self._instance_value_path)

    @property
    def attributes(self):
        return dict(self._attributes)

    def __init__(self, *, type_identifier, default_value='', instance_value_path='', attributes=None, **kwargs):
        super().__init__(**kwargs)

        if attributes is None:
            attributes = dict()

        self._type = type_identifier
        self._default_value = default_value
        self._instance_value_path = instance_value_path
        self._attributes = attributes

    def pack(self):
        result = super().pack()

        result['type'] = self.type
        result['default_value'] = self.default_value
        result['attributes'] = self.attributes
        return result

    def derive_default_value(self, item=None):

        if item is None or not self.instance_value_path_components:
            return self.default_value

        return value_at_dotted_path(item, self.instance_value_path_components, default=self.default_value)

    # noinspection PyMethodMayBeStatic
    def clean_value(self, value):
        return value


class TextAreaAnnotationField(ContentAnnotationField):

    def __init__(self, **kwargs):

        default_value = kwargs.pop('default_value', '')

        super().__init__(type_identifier='textarea', default_value=default_value, **kwargs)


class TextAnnotationField(ContentAnnotationField):

    def __init__(self, **kwargs):

        default_value = kwargs.pop('default_value', '')

        super().__init__(type_identifier='text', default_value=default_value, **kwargs)


class NumberAnnotationField(ContentAnnotationField):

    def __init__(self, **kwargs):

        default_value = kwargs.pop('default_value', '0')

        super().__init__(type_identifier='number', default_value=default_value, **kwargs)

    # noinspection PyMethodMayBeStatic
    def clean_value(self, value):

        if not value:
            return None

        try:
            value = int(value)
            return value
        except ValueError:
            pass

        try:
            value = float(value)
            return value
        except ValueError as error:
            raise error


class RadioButtonAnnotationField(ContentAnnotationField):

    def __init__(self, **kwargs):

        default_value = kwargs.pop('default_value', False)

        super().__init__(type_identifier='radio', default_value=default_value, **kwargs)


class CheckboxAnnotationField(ContentAnnotationField):

    def __init__(self, **kwargs):
        default_value = kwargs.pop('default_value', False)

        super().__init__(type_identifier='checkbox', default_value=default_value, **kwargs)


class ChoiceAnnotationField(ContentAnnotationField):

    def __init__(self, **kwargs):

        attributes = dict(kwargs.pop('attributes', {}))
        choices = attributes.pop('choices', [])
        attributes['choices'] = choices

        default_value = choices[0][0] if choices else ''
        default_value = kwargs.pop('default_value', default_value)

        super().__init__(type_identifier='choice', default_value=default_value, attributes=attributes, **kwargs)


"""

    def _build_block_json(self):
        self._js_context = JSContext()
        self._block_json = json.dumps(self._js_context.pack(self.block_def))

    @property
    def js_context(self):
        if self._js_context is None:
            self._build_block_json()

        return self._js_context

    @property
    def block_json(self):
        if self._js_context is None:
            self._build_block_json()

        return self._block_json

"""


class TelepathWidgetAnnotationField(ContentAnnotationField):

    def create_widget_factory(self):
        return None

    def classname(self):
        return ''

    def __init__(self, widget_state=None, **kwargs):
        default_value = kwargs.pop('default_value', '')

        if not default_value:
            default_value = ''

        self.widget_state = widget_state

        super().__init__(type_identifier='telepath_widget', default_value=default_value, **kwargs)

    def pack(self):
        result = super().pack()

        widget_factory = self.create_widget_factory()

        js_context = JSContext()
        widget_factory = js_context.pack(widget_factory)

        attributes = {
            'widgetFactory': widget_factory,
            'widgetState': self.widget_state,
            'classname': self.get_classname()
        }

        attributes.update(self.attributes)

        result['type'] = self.type
        result['default_value'] = self.default_value
        result['attributes'] = attributes
        return result


class ExperimentalPageChooserAnnotationField(TelepathWidgetAnnotationField):

    def create_widget_factory(self):
        return AdminPageChooser(target_models=["wagtailcore.Page"])

    def get_classname(self):
        return 'w-field--admin_page_chooser'

    def __init__(self, **kwargs):
        default_value = kwargs.pop('default_value', '')

        if not default_value:
            default_value = ''

        widget_state = default_value

        super().__init__(default_value=default_value, widget_state=widget_state, **kwargs)


class PageChooserAnnotationField(NumberAnnotationField):

    def __init__(self, **kwargs):
        default_value = kwargs.pop('default_value', None)

        if not default_value:
            default_value = None

        super().__init__(default_value=default_value, **kwargs)


class ContentAnnotationGroup(BaseDescriptor):

    @property
    def fields(self):
        return self._fields[:]

    def __init__(self, *, fields=None, **kwargs):
        super().__init__(**kwargs)

        if fields is None:
            fields = []

        self._fields = list(fields)

    def pack(self):
        result = super().pack()
        result['fields'] = [field.pack() for field in self.fields]

        return result

    def clean_annotations_for_item(self, annotations, item, wipe=True):

        result = annotations if not wipe else {}

        for field in self.fields:
            value = annotations.setdefault(field.identifier, field.derive_default_value(item))
            value = field.clean_value(value)
            result[field.identifier] = value

        return result


class ContentAnnotationsRegistry:

    def __init__(self):
        self.__entries = {}

    def register(self, annotations):
        self.__entries[annotations.identifier] = annotations

    def lookup(self, identifier, default=None):
        return self.__entries.get(identifier, default)


CONTENT_ANNOTATIONS_REGISTRY = ContentAnnotationsRegistry()


@deconstructible
class ContentAnnotations:

    @property
    def groups(self):
        return self._groups[:]

    @property
    def identifier(self):
        return str(id(self))

    def __init__(self, *, groups=None):

        if groups is None:
            groups = []

        self._groups = list(groups)

        CONTENT_ANNOTATIONS_REGISTRY.register(self)

    def pack(self):

        panels = []

        for group in self.groups:
            panels.append(group.pack())

        result = {"panels": panels}
        return result

    # noinspection PyMethodMayBeStatic
    def clean(self, items, annotations=None, wipe=True):

        if annotations is None or (items and not annotations):
            annotations = [{} for _ in range(len(items))]
        else:
            annotations = list(annotations)

        for index, item_annotations in enumerate(annotations):

            item = items[index]
            cleaned = item_annotations if not wipe else {}

            if item_annotations is None:
                item_annotations = {}

            for group in self.groups:

                group_annotations = item_annotations.setdefault(group.identifier, {})
                group_annotations = group.clean_annotations_for_item(group_annotations, item, wipe=wipe)
                cleaned[group.identifier] = group_annotations

            annotations[index] = cleaned

        return annotations

    @classmethod
    def lookup(cls, identifier, default=None):
        return CONTENT_ANNOTATIONS_REGISTRY.lookup(identifier, default)
