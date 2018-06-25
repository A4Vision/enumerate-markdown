from enumerate_markdown import enumerator
from enumerate_markdown import headers_finder


class EnumerationFormatter(object):
    def format(self, full_index):
        return '.'.join(map(str, full_index)) + ' '


def enumerate_headers(text, finder=headers_finder.HeadersFinder(), enumeration_formatter=EnumerationFormatter()):
    e = enumerator.Enumerator()
    headers = finder.find_headers(text)
    prev_offset = 0
    res = ''
    for header in headers:
        assert header.offset() >= prev_offset
        header.advance_enumerator(e)
        res += text[prev_offset: header.offset()] + enumeration_formatter.format(e.get_index())
        prev_offset = header.offset()
    res += text[prev_offset:]
    return res
