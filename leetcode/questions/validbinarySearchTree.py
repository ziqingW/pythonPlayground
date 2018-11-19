# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:

# Input:
#     2
#   / \
#   1   3
# Output: true
# Example 2:

#     5
#   / \
#   1   4
#      / \
#     3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
#              is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node):
            if not node:
                return
            if not node.left and not node.right:
                breadth.append(node.val)
            else:
                if helper(node.left) is not None:
                    breadth.append(helper(node.left))
                breadth.append(node.val)
                if helper(node.right) is not None:
                    breadth.append(helper(node.right))
            
        breadth = []
        helper(root)
        return breadth == sorted(breadth) and len(breadth) == len(set(breadth))
            
            
#  not very satisfied with this method, which takes NlogN complexicity.