import re


FIND_BLOCK_KEY_ATTR = re.compile(r'\s*data-block-key\s*=\s*"([^"]*)"\s*')


class BlockKeyRewriter:

    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def handle_block_key(self, match):
        return ''

    def __call__(self, html):
        return FIND_BLOCK_KEY_ATTR.sub(self.handle_block_key, html)
