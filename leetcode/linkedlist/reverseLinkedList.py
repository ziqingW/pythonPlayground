# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n_head = head
        n_tail = n_head
        while n_head is not None and n_head.next is not None:
            n_next = n_head.next
            n_head.next = n_head.next.next       
            n_next.next = n_tail
            n_tail = n_next
        return n_tail