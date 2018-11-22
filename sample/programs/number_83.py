# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next    # skip duplicated node
            head = head.next     # not duplicate of current node, move to next node
        return dummy