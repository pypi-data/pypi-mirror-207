
from django.utils.functional import cached_property
from django.forms import Media

from wagtail.hooks import get_hooks

from wagtail.admin.rich_text.editors.draftail import DraftailRichTextArea as DefaultRichTextArea

__all__ = ['DraftailRichTextArea']

from .apps import get_app_label

APP_LABEL = get_app_label()

REGISTERED_RICH_TEXT_AREA_MEDIA_SETTINGS = []
HAS_REGISTERED_HOOKS = False


def register_rich_text_area_media_settings(media_settings):
    REGISTERED_RICH_TEXT_AREA_MEDIA_SETTINGS.append(media_settings)


def load_rich_text_area_media_settings():

    if HAS_REGISTERED_HOOKS:
        return REGISTERED_RICH_TEXT_AREA_MEDIA_SETTINGS

    for hook in get_hooks('register_rich_text_area_media_settings'):
        register_rich_text_area_media_settings(hook())

    return REGISTERED_RICH_TEXT_AREA_MEDIA_SETTINGS


# noinspection SpellCheckingInspection
class DraftailRichTextArea(DefaultRichTextArea):

    """
    To use this for a StreamField, the following conditions have to be met:

    (1) In settings/base.py, add
        WAGTAILADMIN_RICH_TEXT_EDITORS = {
            'wagtail_richer_text.richtextarea': {
                'WIDGET': 'wagtail_richer_text.widgets.DraftailRichTextArea'
            }
        }

    (2) When initialising a StreamBlock, pass editor="concisely.richtextarea"

    """

    template_name = 'wagtail_richer_text/widgets/draftail_rich_text_area.html'

    def __init__(self, *args, **kwargs):

        default_attrs = {}
        attrs = kwargs.get('attrs')
        if attrs:
            default_attrs.update(attrs)
        kwargs['attrs'] = default_attrs

        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        return context

    @cached_property
    def media(self):
        media = super().media

        for settings in load_rich_text_area_media_settings():
            media = media + Media(**settings)

        return media