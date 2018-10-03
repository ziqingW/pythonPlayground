# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != head:
                    head = head.next
                    slow = slow.next
                return head
        return None
        
#     a           b
# head ---> start----> meet
#             |           |
#             <-----------
#                 c
# slow: a+b+r1(c+b)
# fast: a+b+r2(c+b) = 2* slow
# a = (n-1)(b+c) +c
# which means, if slow starts to move when meeted with fast, and head starts moving too
# after slow moves several cycles and c steps, it will meet with head eventually!