# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        result = []
        t = 1
        while level:
            nextLevel = []
            levelVals = []
            for node in level:
                levelVals.append(node.val)
                if t % 2 == 1:
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
                else:
                    if node.right:
                        nextLevel.append(node.right)
                    if node.left:
                        nextLevel.append(node.left)
                nextLevel = nextLevel[::-1]
                result.append(levelVals)
                level = nextLevel
                t += 1
        return result
