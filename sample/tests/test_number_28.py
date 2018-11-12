import unittest

from sample.programs.number_28 import Solution


class TestNumber28(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.strStr('hello', 'll'), 2)
        self.assertEqual(self.solution.strStr(
            'aaaaa', 'bba'), -1)
        self.assertEqual(self.solution.strStr(
            'aaaaa', ''), 0)


if __name__ == '__main__':
    unittest.main()
