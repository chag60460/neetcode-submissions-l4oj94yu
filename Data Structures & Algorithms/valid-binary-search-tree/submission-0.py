# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, float("-inf"), float("inf"))
    def is_valid(self, node, left, right):
        if not node:
            return True
        
        if not (node.val > left and node.val < right):
            return False
        
        return self.is_valid(node.left, left, node.val) and self.is_valid(node.right, node.val, right)