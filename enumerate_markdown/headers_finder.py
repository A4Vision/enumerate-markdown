import re
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
    HEADING_PATTERN   = re.compile('^([\t ]*(#{1,6}))[^#\n][\t ]*\\S')
    L_HEADING_PATTERN = re.compile('^^([\t ]*\n)[ \t]*[^\n]*[^\n \t][^\n]*\n[\t ]*(=|-)+[\t ]*\n')

    def find_headers(self, text):
        text = '\n' + text + '\n'
        headers = []
        chars_remover = CharsRemover(text)
        while chars_remover.has_chars():
            current_header = self._get_header(chars_remover.current_text(), chars_remover.get_offset() - 1)
            if current_header is None:
                chars_remover.remove_first_line()
            else:
                headers.append(current_header)
                chars_remover.remove_first_line()
        return headers

    def _get_match(self, text):
        for p in (HeadersFinder.HEADING_PATTERN, HeadersFinder.L_HEADING_PATTERN):
            if p.match(text):
                return p.match(text)

    def _get_level(self, group2):
        if '#' in group2:
            return len(group2)
        else:
            return {'-': 2, '=': 1}[group2]

    def _get_header(self, text, base_offset):
        m = self._get_match(text)
        if m:
            header_offset = len(m.group(1))
            level = self._get_level(m.group(2))
            return header.Header(base_offset + header_offset, level)


