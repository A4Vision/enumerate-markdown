import unittest

from enumerate_markdown import enumerator


class EnumeratorTest(unittest.TestCase):
    def testAdvance(self):
        e = enumerator.Enumerator()
        self.assertEqual(e.get_index(), tuple())
        e.add_enumerate(1)
        self.assertEqual(e.get_index(), (1,))
        e.add_enumerate(1)
        self.assertEqual(e.get_index(), (2,))
        e.add_enumerate(3)
        self.assertEqual(e.get_index(), (2, 1, 1,))
        e.add_enumerate(3)
        self.assertEqual(e.get_index(), (2, 1, 2,))
        e.add_enumerate(1)
        self.assertEqual(e.get_index(), (3,))

    def testWithMinimalLevel(self):
        e = enumerator.EnumeratorWithMinimalLevel(2)
        self.assertEqual(e.get_index(), tuple())
        e.add_enumerate(1)
        self.assertEqual(e.get_index(), tuple())
        e.add_enumerate(2)
        self.assertEqual(e.get_index(), (1,))
        e.add_enumerate(3)
        self.assertEqual(e.get_index(), (1, 1,))
        e.add_enumerate(3)
        self.assertEqual(e.get_index(), (1, 2,))
        e.add_enumerate(2)
        self.assertEqual(e.get_index(), (2,))
