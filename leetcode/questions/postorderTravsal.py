# Given a binary tree, return the postorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#   1
#     \
#      2
#     /
#   3

# Output: [3,2,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        if root: stack.append(root)
        while stack:
            node = stack.pop()
            result.insert(0, node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return result
        
            