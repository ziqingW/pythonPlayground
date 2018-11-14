# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#   / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#   / \
#   2   2
#   \   \
#   3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [root]
        while True:
            level = []
            for node in queue:
                if node != "null":
                    if node.left:
                        level.append(node.left)
                    else:
                        level.append("null")
                    if node.right:
                        level.append(node.right)
                    else:
                        level.append("null")
            results = [node for node in level if node != "null"]
            if not results:
                return True
            values = [node.val if node != "null" else "null" for node in level]
            if values[::-1] != values:
                return False
            queue = level
            