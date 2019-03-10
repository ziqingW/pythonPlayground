# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than p.val.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if len(result) == 0 and node == p:
                result.append(node)
            elif len(result) == 1:
                result.append(node)
            inorder(node.right)

        result = []
        inorder(root)
        if len(result) > 1:
            return result[-1]
        return None
