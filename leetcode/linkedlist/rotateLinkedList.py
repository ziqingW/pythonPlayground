# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        size = 0
        if head:
            size = 1
            curr = head
            while curr.next:
                curr = curr.next
                size += 1
            intersection = head
            times = k % size
            if times > 0:
                for i in range(size-times-1):
                    head = head.next
                if head.next:
                    newHead = head.next
                    newCurr = newHead
                    head.next = None
                    while newCurr and newCurr.next:
                        newCurr = newCurr.next
                    newCurr.next = intersection
                    return newHead
        return head
            