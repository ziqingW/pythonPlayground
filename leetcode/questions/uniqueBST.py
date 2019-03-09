# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def generate_subtree(start, end):
            if start > end:
                return [None,]
            else:
                trees = []
                for i in range(start, end+1):
                    leftTree = generate_subtree(start, i-1)
                    rightTree = generate_subtree(i+1, end)
                    for l in leftTree:
                        for r in rightTree:
                            root = TreeNode(i)
                            root.left = l
                            root.right = r
                            trees.append(root)
                return trees

        return generate_subtree(1, n) if n else []
