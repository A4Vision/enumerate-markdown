import functools
import re

import mistune
import mistune.block_parser

from enumerate_markdown import header


class CharsRemover(object):
    def __init__(self, text):
        self._offset = 0
        self._text = text

    def get_offset(self):
        return self._offset

    def has_chars(self):
        return len(self._text) > 0

    def remove_first_line(self):
        if '\n' in self._text:
            chars_to_remove = self._text.index('\n') + 1
        else:
            chars_to_remove = len(self._text)
        self.remove_chars(chars_to_remove)

    def remove_chars(self, chars_to_remove):
        self._text = self._text[chars_to_remove:]
        self._offset += chars_to_remove

    def current_text(self):
        return self._text


class HeadersFinder(object):
    def __init__(self):
        self._headers_found = []

    def find_headers(self, text):
        self._headers_found = []
        markdown = mistune.create_markdown(renderer="ast")
        new_text, state = markdown.before_parse(text, {})
        markdown.block.SETEX_HEADING = re.compile(r'([^\n]+)\n *(=|-){1,}[ \t]*\n+')
        markdown.block.parse_axt_heading = self.decorate_parse_axt_heading(markdown.block.parse_axt_heading)
        markdown.block.parse_setex_heading = self.decorate_parse_setex_heading(markdown.block.parse_setex_heading)
        markdown.block.parse(new_text, state)
        return new_text, self._headers_found

    def decorate_parse_axt_heading(self, parse_heading_func):
        @functools.wraps(parse_heading_func)
        def wrapper(m, state):
            level = len(m.group(1))
            self._headers_found.append(header.Header(m.regs[1][0] + level, level))
            return parse_heading_func(m, state)

        return wrapper

    def decorate_parse_setex_heading(self, parse_heading_func):
        @functools.wraps(parse_heading_func)
        def wrapper(m, state):
            level = 1 if m.group(2) == '=' else 2
            self._headers_found.append(header.Header(m.start(), level))
            return parse_heading_func(m, state)

        return wrapper
