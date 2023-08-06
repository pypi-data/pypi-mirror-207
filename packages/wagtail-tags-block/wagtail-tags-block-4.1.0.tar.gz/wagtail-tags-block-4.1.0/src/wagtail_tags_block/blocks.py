
from django.utils.functional import cached_property

from wagtail.blocks import FieldBlock
from wagtail.admin.widgets import AdminTagWidget
from wagtail.coreutils import resolve_model_string

from taggit.forms import TagField


__all__ = ['TagsBlock', 'TagsValue']


class TagsValue(list):

    def __init__(self, iterable, block=None):
        super().__init__(iterable)

        self.block = block

    def __html__(self):
        return self.block.render(self)

    def render_as_block(self, context=None):
        return self.block.render(self, context=context)


class TagsBlock(FieldBlock):

    class Meta:
        value_class = TagsValue
        tag_model = None
        free_tagging = None

        classname = "tags"
        tag_classname = "tag"
        container_element = "div"

    @cached_property
    def tag_model(self):
        return resolve_model_string(self.meta.tag_model)

    def __init__(self, *, required=False, help_text=None, **kwargs):

        tag_model = kwargs.pop('tag_model', self._meta_class.tag_model)
        free_tagging = kwargs.pop('free_tagging', self._meta_class.free_tagging)
        value_class = kwargs.pop('value_class', self._meta_class.value_class)

        super().__init__(tag_model=tag_model, free_tagging=free_tagging, value_class=value_class,
                         required=required, help_text=help_text, **kwargs)

    @cached_property
    def field(self):
        widget = AdminTagWidget(tag_model=self.tag_model, free_tagging=self.meta.free_tagging)
        return TagField(widget=widget, help_text=self.meta.help_text, required=self.meta.required)

    def get_default(self):
        return self.meta.value_class((), block=self)

    def value_from_form(self, value):

        result = []

        for tag_name in value:
            tag, _ = self.tag_model.objects.get_or_create(name=tag_name)
            result.append(tag)

        result = self.meta.value_class(result, self)
        return result

    def value_for_form(self, value):

        result = []

        for tag in value:
            result.append(tag.name)

        return result

    def to_python(self, value):

        if isinstance(value, self.meta.value_class):
            return value

        if not value:
            return self.meta.value_class((), block=self)

        return self.value_from_form(value)

    def get_prep_value(self, value):
        return self.value_for_form(value)

    def get_context(self, value, parent_context=None):
        """
        Return a dict of context variables (derived from the block value and combined with the parent_context)
        to be used as the template context when rendering this value through a template.
        """

        context = super(TagsBlock, self).get_context(value, parent_context)

        context.update(
            {
                "block": self
            }
        )

        return context
