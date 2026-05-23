# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs_good_nodes(root, root.val)

    def dfs_good_nodes(self, node, maxVal):
        if not node:
            return 0
        
        good_node_count = 0
        if node.val >= maxVal:
            maxVal = node.val
            good_node_count = 1
        
        return good_node_count + self.dfs_good_nodes(node.left, maxVal) + self.dfs_good_nodes(node.right, maxVal)