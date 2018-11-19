# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

#         _______3______
#       /              \
#     ___5__          ___1__
#   /      \        /      \
#   6      _2       0       8
#          /  \
#          7   4
# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of of nodes 5 and 1 is 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # base condition for none
        if not root:
            return None
        # current node condition         
        if root.val == p.val or root.val == q.val:
            return root
        # children condition
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        # if both left and right not None, root is the LCA
        if left and right:
            return root
        # if one side is None, which means the other side is the LCA (both nodes are in one side)
        else:
            return left if left else right
            