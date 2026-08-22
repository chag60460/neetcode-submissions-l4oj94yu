# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.findMaxHeight(root)
        return self.diameter
    
    def findMaxHeight(self, root):
        if not root:
            return -1
        
        left_height = self.findMaxHeight(root.left)
        right_height = self.findMaxHeight(root.right)

        self.diameter = max(self.diameter, left_height + right_height + 2)

        return 1 + max(left_height, right_height)