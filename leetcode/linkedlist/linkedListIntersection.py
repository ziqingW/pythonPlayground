# Write a program to find the node at which the intersection of two singly linked lists begins.


# For example, the following two linked lists:

# A:          a1 → a2
#                   ↘
#                      c1 → c2 → c3
#                   ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        link_a = headA
        link_b = headB
        while link_a is not None and link_b is not None:
            if link_a == link_b:
                return link_a
            link_a = link_a.next
            link_b = link_b.next
            if link_a is None and link_b is not None:
                link_a = headB
            if link_b is None and link_a is not None:
                link_b = headA
        return None