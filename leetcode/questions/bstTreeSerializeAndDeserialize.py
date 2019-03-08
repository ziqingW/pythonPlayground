# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        def preorder(node):
            if node:
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ' '.join(map(str, result))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = list(map(int, data.split()))
        def build(minValue, maxValue):
            if data and minValue < data[0] < maxValue:
                val = data.pop(0)
                node = TreeNode(val)
                node.left = build(minValue, val)
                node.right = build(val, maxValue)
                return node
        return build(float('-infinity'), float('infinity'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
