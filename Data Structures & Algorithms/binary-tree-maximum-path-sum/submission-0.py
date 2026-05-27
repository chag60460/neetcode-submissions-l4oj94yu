# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = [root.val]
        self.compute_max_dfs(root)
        return self.result[0]
    
    def compute_max_dfs(self, root):
        if not root:
            return 0

        leftMax = self.compute_max_dfs(root.left)
        rightMax = self.compute_max_dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        #max path sum WITH split
        self.result[0] = max(self.result[0], root.val + leftMax + rightMax)

        #return max path sum WITHOUT split
        return root.val + max(leftMax, rightMax)