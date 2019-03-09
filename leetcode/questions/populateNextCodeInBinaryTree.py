# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            level = [root]
            while level:
                nextLevel = []
                for i in range(len(level)):
                    if i != len(level)-1:
                        level[i].next = level[i+1]
                    if level[i].left:
                        nextLevel.append(level[i].left)
                    if level[i].right:
                        nextLevel.append(level[i].right)
                level = nextLevel
        return root
