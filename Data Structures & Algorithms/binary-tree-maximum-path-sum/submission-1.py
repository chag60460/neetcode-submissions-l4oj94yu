# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.dfs_find_max(root)

        return self.result

    def dfs_find_max(self, root):
        if not root:
            return 0
        
        leftMax = self.dfs_find_max(root.left)
        rightMax = self.dfs_find_max(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        self.result = max(self.result, root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)