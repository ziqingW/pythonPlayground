# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        slow = fast = head
        while head is not None:
            if head.val == val:
                head = head.next
                slow = fast = head
            else:
                break
        while fast is not None:
            fast = fast.next
            if fast is None:
                slow.next = fast
                slow = slow.next
            else:
                if fast.val != val:
                    slow.next = fast
                    slow = slow.next
        return head
                