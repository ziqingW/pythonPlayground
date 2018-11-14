# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# Example :

# Input:  root = [5,1,5,5,5,null,5]

#               5
#              / \
#             1   5
#           / \   \
#           5   5   5

# Output: 4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def singlyHelper(self, root, count):
        if not root:
            return True
        left = self.singlyHelper(root.left, count)
        right = self.singlyHelper(root.right, count)
        if left == False or right == False:
            return False
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        count[0] += 1
        return True   
        
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        self.singlyHelper(root, count)
        return count[0]
        