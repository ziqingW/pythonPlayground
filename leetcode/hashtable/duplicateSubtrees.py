# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with same node values.

# Example 1:

#         1
#       / \
#       2   3
#      /   / \
#     4   2   4
#       /
#       4
# The following are two duplicate subtrees:

#       2
#      /
#     4
# and

#     4
# Therefore, you need to return above trees' root in the form of a list.

class Solution:
    def findDuplicateSubtrees(self, root):
            def trv(root):
                if not root: return "null"
                struct = "{},{},{}".format(root.val, trv(root.left), trv(root.right))
                nodes[struct].append(root)
                return struct

            nodes = collections.defaultdict(list)
            trv(root)
            return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]
            

            