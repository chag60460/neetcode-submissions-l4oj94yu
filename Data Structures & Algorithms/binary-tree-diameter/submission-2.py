# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.find_max_height(root)

        return self.diameter
    
    def find_max_height(self, root):
        if not root:
            return 0
        
        left_height = self.find_max_height(root.left)
        right_height = self.find_max_height(root.right)

        self.diameter = max(self.diameter, left_height+right_height)
        
        return 1 + max(left_height, right_height)