import unittest

from sample.programs.number_13 import Solution


class TestNumber13(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.romanToInt('III'), 3)
        self.assertEqual(self.solution.romanToInt('IV'), 4)
        self.assertEqual(self.solution.romanToInt('MCMXCIV'), 1994)
        self.assertEqual(self.solution.romanToInt('IX'), 9)
        # self.assertEqual(self.solution.romanToInt('LVIII'), 58)


if __name__ == '__main__':
    unittest.main()
