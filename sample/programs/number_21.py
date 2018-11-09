class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def get_list_nodes(list_data):
        dummy = list_node = ListNode(-1)
        for data in list_data:
            list_node.next = ListNode(data)
            list_node = list_node.next
        return dummy.next

    @staticmethod
    def format_listnode(list_node):
        return_list = []
        while list_node:
            return_list.append(list_node.val)
            list_node = list_node.next
        return return_list


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        dummy = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
