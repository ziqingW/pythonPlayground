# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        else:
            curr = head
            copyHead = RandomListNode(head.label)
            copyHead.next = RandomListNode(curr.next.label) if curr.next else None
            copyHead.random = RandomListNode(curr.random.label) if curr.random else None
            copycurr = copyHead
            while curr and curr.next:
                curr = curr.next
                copycurr = copycurr.next
                copycurr.next = RandomListNode(curr.next.label) if curr.next else None
                copycurr.random = RandomListNode(curr.random.label) if curr.random else None
            return copyHead
            