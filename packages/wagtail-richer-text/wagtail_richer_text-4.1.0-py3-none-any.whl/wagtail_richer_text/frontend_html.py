
from wagtail.hooks import get_hooks
from wagtail.rich_text import expand_db_html as default_expand_db_html, RichText as DefaultRichText
from wagtail.rich_text.rewriters import MultiRuleRewriter
from .block_key_rewriter import BlockKeyRewriter

__all__ = ['RichText', 'register_rich_text_rewriter', 'expand_db_html']


FRONTEND_REWRITER = None

REGISTERED_REWRITERS = []
HAS_REGISTERED_HOOKS = False


def register_rich_text_rewriter(rewriter):
    REGISTERED_REWRITERS.append(rewriter)


def load_rich_text_rewriters():

    if HAS_REGISTERED_HOOKS:
        return REGISTERED_REWRITERS

    for hook in get_hooks('register_rich_text_rewriter'):
        register_rich_text_rewriter(hook())

    return REGISTERED_REWRITERS


def expand_db_html(html):
    """
    Expand database-representation HTML into proper HTML usable on front-end templates
    """
    global FRONTEND_REWRITER

    if FRONTEND_REWRITER is None:

        FRONTEND_REWRITER = MultiRuleRewriter([
            BlockKeyRewriter()
        ] + load_rich_text_rewriters())

    result = FRONTEND_REWRITER(html)
    result = default_expand_db_html(result)
    return result


class RichText(DefaultRichText):

    """
    Overrides the built-in wagtail version to allow for front-end rewriting.
    """

    def __init__(self, source):
        super().__init__(source)

    def __html__(self):
        source = self.source
        source = expand_db_html(source)
        return source
