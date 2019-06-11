import unittest

import pattern

class TestPattern(unittest.TestCase):

    def test_positive(self):
        self.assertTrue(pattern.has_pattern('000'))
        self.assertTrue(pattern.has_pattern('11010110101'))
        self.assertTrue(pattern.has_pattern('11001010011001'))

    def test_negative(self):
        self.assertFalse(pattern.has_pattern('001'))
        self.assertFalse(pattern.has_pattern('11010011001'))
        self.assertFalse(pattern.has_pattern('11001101001100'))

if __name__ == '__main__':
    unittest.main()
