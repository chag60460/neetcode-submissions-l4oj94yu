# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        self.dfs(root, k)

        return self.result
    
    def dfs(self, node, k):
        if not node:
            return
        
        self.dfs(node.left, k)
        self.count += 1
        
        if self.count == k:
            self.result = node.val
            return
        
        self.dfs(node.right, k)


