# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(instart, inend):
            if instart > inend:
                return None
            if helper.postIndex > -1:
                tNode = TreeNode(postorder[helper.postIndex])
                helper.postIndex -= 1
                if instart == inend:
                    return tNode
                inIndex = hashmap[tNode.val]
                tNode.right = helper(inIndex+1, inend)
                tNode.left = helper(instart, inIndex - 1)
                return tNode
        
        if len(inorder) == 0:
            return None
        helper.postIndex = len(postorder)-1
        hashmap = {v:k for k,v in enumerate(inorder)}
        return helper(0, len(inorder)-1)
            