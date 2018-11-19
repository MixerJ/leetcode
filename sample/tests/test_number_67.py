import unittest

from sample.programs.number_67 import Solution


class TestNumber67(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.addBinary(
            "11", "1"), "100")
        self.assertEqual(self.solution.addBinary(
            "1010", "1011"), "10101")


if __name__ == '__main__':
    unittest.main()
