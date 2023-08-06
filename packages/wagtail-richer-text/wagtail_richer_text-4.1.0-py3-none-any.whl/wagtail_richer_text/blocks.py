

from wagtail.blocks import RichTextBlock as DefaultBlock

from .apps import get_app_label
from .frontend_html import RichText

__all__ = ['RichTextBlock']

APP_LABEL = get_app_label()


class RichTextBlock(DefaultBlock):

    class Meta:
        default = ''

    def __init__(self, *args, **kwargs):

        if 'editor' not in kwargs:
            kwargs['editor'] = 'wagtail_richer_text.richtextarea'

        super().__init__(*args, **kwargs)

    def deconstruct(self):
        _, args, kwargs = super(RichTextBlock, self).deconstruct()
        path = APP_LABEL + '.blocks.RichTextBlock'
        return path, args, kwargs

    def get_default(self):
        if isinstance(self.meta.default, RichText):
            return self.meta.default
        else:
            return RichText(self.meta.default)

    def to_python(self, value):
        # convert a source-HTML string from the JSONish representation
        # to a RichText object
        return RichText(value)

    def value_from_form(self, value):
        # Rich text editors return a source-HTML string; convert to a RichText object
        return RichText(value)
