# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr1 = l1
        curr2 = l2
        result = l1
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if curr1.val < curr2.val:
                curr1 = curr1.next
            else:
                result = l2
                curr2 = curr2.next
            result_curr = result
            while curr1 is not None and curr2 is not None:
                
                if curr1.val < curr2.val:
                    result_curr.next = curr1
                    curr1 = curr1.next
                else:
                    result_curr.next = curr2
                    curr2 = curr2.next
                result_curr = result_curr.next
            if curr1 is None:
                result_curr.next = curr2
            elif curr2 is None:
                result_curr.next = curr1
            return result
                
            