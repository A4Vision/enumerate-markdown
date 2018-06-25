import unittest
from enumerate_markdown import enumerate_markdown, header


class MyHeadersFinder(object):
    def __init__(self, headers):
        self._headers = headers

    def find_headers(self, text):
        return self._headers


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
        text = "ABCDE"
        enumerated_text = enumerate_markdown.enumerate_headers(text, headers_finder)
        expected_enumerated = "1 AB1.1 CD2 E"
        self.assertEqual(expected_enumerated, enumerated_text)
