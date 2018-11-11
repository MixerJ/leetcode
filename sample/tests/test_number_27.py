import unittest

from sample.programs.number_27 import Solution


class TestNumber26(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_success(self):
        self.assertEqual(self.solution.removeElement([3, 2, 2, 3], 3), 2)
        self.assertEqual(self.solution.removeElement(
            [0, 1, 2, 2, 3, 0, 4, 2], 2), 5)


if __name__ == '__main__':
    unittest.main()
