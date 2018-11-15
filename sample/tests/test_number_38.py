import unittest

from sample.programs.number_38 import Solution


class TestNumber38(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.countAndSay(1), "1")
        self.assertEqual(self.solution.countAndSay(4), "1211")


if __name__ == '__main__':
    unittest.main()
