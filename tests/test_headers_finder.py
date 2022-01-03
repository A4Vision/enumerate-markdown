import unittest

from enumerate_markdown import headers_finder, header


class HeadersFinderTest(unittest.TestCase):

    def test_find_headers(self):
        text = """## Header 1 (level=2)
        
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
 Header 6 above
        
 Header 7 
  ---"""

        finder = headers_finder.HeadersFinder()
        next_text, headers = finder.find_headers(text)

        header1 = header.Header(next_text.find(" Header 1"), 2)
        header2 = header.Header(next_text.find(" Header 2"), 2)
        header3 = header.Header(next_text.find(" Header 3"), 1)
        header4 = header.Header(next_text.find(" Header 4"), 4)
        header5 = header.Header(next_text.find(" Header 5"), 1)
        header6 = header.Header(next_text.find(" Header 6 above") - 1, 4)
        header7 = header.Header(next_text.find(" Header 7"), 2)
        expected_headers = [header1, header2, header3, header4, header5, header6, header7]

        self.assertListEqual(expected_headers, headers)

    def test_find_headers_with_code_block(self):
        text = """

def foo():
    print(1)
foo()
text = '''
# Header 1

abc ** def **
    ```python
    x = 123
    # not header
    x = 456
  # Header 2 #   

    ```
 Header 3
===

hi # not header
### Header 4
        """
        finder = headers_finder.HeadersFinder()
        next_text, headers = finder.find_headers(text)
        header1 = header.Header(next_text.find(" Header 1"), 1)
        header2 = header.Header(next_text.find(" Header 2"), 1)
        header3 = header.Header(next_text.find(" Header 3"), 1)
        header4 = header.Header(next_text.find(" Header 4"), 3)
        expected_headers = [header1, header2, header3, header4]
        self.assertListEqual(expected_headers, headers)

    def test_with_chinese(self):
        text = """# 电子现金指定账户圈存
"""
        finder = headers_finder.HeadersFinder()
        next_text, headers = finder.find_headers(text)
        header1 = header.Header(next_text.find(" 电子现金指定账户圈存"), 1)
        expected_headers = [header1]
        self.assertListEqual(expected_headers, headers)
