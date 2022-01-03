import unittest

from enumerate_markdown import enumerate_markdown, header


class MyHeadersFinder(object):
    def __init__(self, headers):
        self._headers = headers

    def find_headers(self, text):
        return text, self._headers


class MyEnumerator(object):
    def __init__(self, indices):
        assert len(indices) > 0
        self._indices = indices
        self._current = 0

    def add_enumerate(self, level):
        pass

    def get_index(self):
        value = self._indices[self._current]
        self._current += 1
        if self._current == len(self._indices):
            self._current = 0
        return value


class EnumerateMarkdownTest(unittest.TestCase):
    def test_enumerate_headers(self):
        headers = [header.Header(0, 1), header.Header(2, 2), header.Header(4, 1)]
        headers_finder = MyHeadersFinder(headers)
        text = "ABCD 5. E"
        enumerated_text = enumerate_markdown.enumerate_headers(text, headers_finder)
        expected_enumerated = " 1. AB 1.1 CD 2. E"
        self.assertEqual(expected_enumerated, enumerated_text)

    def test_enumeration_formatter(self):
        formatter = enumerate_markdown.EnumerationFormatter()
        for index in [(1,), (1, 1), (2,), (1, 2, 3)]:
            formatted = formatter.format(index)
            text = formatted + 'some text'
            length = formatter.old_enumeration_length(text)
            self.assertEqual(len(formatted), length)
