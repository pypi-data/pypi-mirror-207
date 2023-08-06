import re

from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from wagtail.rich_text import RichText as DefaultRichText

from ..frontend_html import RichText, expand_db_html

register = template.Library()


@register.filter # noqa
def richertext(value):

    if isinstance(value, RichText):
        return value
    elif isinstance(value, DefaultRichText):
        return RichText(value.source) # noqa
    elif value is None:
        html = ""
    elif isinstance(value, str):
        html = expand_db_html(value)
    else:
        raise TypeError(
            "'richertext' template filter received an invalid value; expected string, got {}.".format(
                type(value)
            )
        )

    return render_to_string("wagtailcore/shared/richtext.html", {"html": html})


P_TAG_RE = re.compile(r'<p( data-block-key="[^"]*")?>|</p>')


@register.filter
def strip_paragraphs(value):


    if isinstance(value, RichText):
        return RichText(P_TAG_RE.sub("", value.source))
    elif isinstance(value, DefaultRichText):
        return RichText(P_TAG_RE.sub("", value.source))
    elif value is None:
        html = ""
    elif isinstance(value, str):
        html = expand_db_html(value)
    else:
        raise TypeError(
            "'richertext' template filter received an invalid value; expected string, got {}.".format(
                type(value)
            )
        )

    html = P_TAG_RE.sub("", html)
    html = mark_safe(html)
    return html
