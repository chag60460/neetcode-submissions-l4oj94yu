# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bfs_is_valid_bst(root, float("-inf"), float("inf"))
    
    def bfs_is_valid_bst(self, node, left_bound, right_bound):
        if not node:
            return True
        
        if not (node.val > left_bound and node.val < right_bound):
            return False
        
        return self.bfs_is_valid_bst(node.left, left_bound, node.val) and self.bfs_is_valid_bst(node.right, node.val, right_bound)