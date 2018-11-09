import unittest

from sample.programs.number_21 import Solution, ListNode


class TestNumber21(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.l1 = ListNode.get_list_nodes([1, 2, 4])
        self.l2 = ListNode.get_list_nodes([1, 3, 4])

    def test_success(self):
        self.assertEqual(ListNode.format_listnode(
            self.solution.mergeTwoLists(self.l1, self.l2)), [1, 1, 2, 3, 4, 4])


if __name__ == '__main__':
    unittest.main()
