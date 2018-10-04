# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Given a singly linked list, determine if it is a palindrome.
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result == result[::-1]
        
        