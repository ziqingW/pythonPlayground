# Given a linked list, remove the n-th node from the end of list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        a1 = head
        k = 0
        while a1 is not None:
            a1 = a1.next
            k += 1
        a1 = head
        if k == n:
            head = head.next
            return head
        elif k - n == 1:
            head.next = head.next.next
            return head
        else:
            for i in range(k-1-n):
                a1 = a1.next
            a1.next = a1.next.next
            return head
            
# method 1: the big O is O(2N)

# method 2: only pass the list for once, the big O is O(N)
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

# my own method, very fast, O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        if head.next == None:
            return None
        curr = head
        if n == 1:
            while True:
                if curr.next.next == None:
                    curr.next = None
                    return head
                else:
                    curr = curr.next
        forward = curr
        while True:
            for i in range(n):
                forward = forward.next
            if forward == None:
                curr.val = curr.next.val
                curr.next = curr.next.next
                return head
            else:
                curr = curr.next
                forward = curr
