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
        
# another method
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # stack = []
        # if not head:
        #     return None
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # newHead = ListNode(stack.pop())
        # curr = newHead
        # while len(stack) > 0:
        #     curr.next = ListNode(stack.pop())
        #     curr = curr.next
        # return newHead
        if not head:
            return None
        if head.next == None:
            return head
        slow = head
        fast = head.next
        tNext = fast.next
        fast.next = slow
        slow.next = None
        while tNext:
            slow = fast
            fast = tNext
            tNext = fast.next
            fast.next = slow
        return fast
        
        