# Given a singly linked list, group all odd nodes together followed by the even nodes. 
# Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        if head is None or head.next is None:
            return head
        even = head.next
        evenHead = head.next
        while odd is not None or even is not None:
            odd.next = even.next
            if odd.next is None:
                odd.next = evenHead
                return head
            odd = odd.next
            even.next = odd.next
            if even.next is None:
                odd.next = evenHead
                return head
            even = even.next
        