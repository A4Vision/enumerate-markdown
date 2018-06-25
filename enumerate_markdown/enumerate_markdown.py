from enumerate_markdown import enumerator


class EnumerationFormatter(object):
    def format(self, full_index):
        return '.'.join(map(str, full_index)) + ' '


def enumerate_headers(text, headers_finder, enumeration_formatter=EnumerationFormatter()):
    e = enumerator.Enumerator()
    headers = headers_finder.find_headers(text)
    prev_offset = 0
    res = ''
    for header in headers:
        assert header.offset() >= prev_offset
        header.advance_enumerator(e)
        res += text[prev_offset: header.offset()] + enumeration_formatter.format(e.get_index())
        prev_offset = header.offset()
    res += text[prev_offset:]
    return res
