import unittest
from enumerate_markdown import headers_finder, header


class HeadersFinderTest(unittest.TestCase):

    def test_find_headers(self):
        text = """## Header 1 (level=1)
        
 Header 2 (level=2)
        ----
        
 Header 3 (level=1)
        =
        
        #### Header 4 (level=4)
        
        not a header #
        # Header 5
        
        not a header
        -- because of this !

####
####
        
 Header 6
        ---"""

        finder = headers_finder.HeadersFinder()
        headers = finder.find_headers(text)
        header1 = header.Header(text.find(" Header 1"), 2)
        header2 = header.Header(text.find(" Header 2"), 2)
        header3 = header.Header(text.find(" Header 3"), 1)
        header4 = header.Header(text.find(" Header 4"), 4)
        header5 = header.Header(text.find(" Header 5"), 1)
        header6 = header.Header(text.find(" Header 6"), 2)
        expected_headers = [header1, header2, header3, header4, header5, header6]

        self.assertListEqual(expected_headers, headers)

