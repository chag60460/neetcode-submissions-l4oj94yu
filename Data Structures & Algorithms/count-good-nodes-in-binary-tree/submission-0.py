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
        
        good_nodes_count = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        good_nodes_count += self.dfs_good_nodes(node.left, maxVal)
        good_nodes_count += self.dfs_good_nodes(node.right, maxVal)

        return good_nodes_count