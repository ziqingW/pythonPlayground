# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#   / \
#   9  20
#     /  \
#   15   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def helper(instart, inend):
            if instart > inend:
                return None
            if helper.preIndex < len(preorder):
                tNode = TreeNode(preorder[helper.preIndex])
                helper.preIndex += 1
                if instart == inend:
                    return tNode
                inIndex = hashmap[tNode.val]
                tNode.left = helper(instart, inIndex-1)
                tNode.right = helper(inIndex + 1, inend)
                return tNode
        
        if len(inorder) == 0:
            return None
        helper.preIndex = 0
        hashmap = {v:k for k,v in enumerate(inorder)}
        return helper(0, len(inorder)-1)
            
