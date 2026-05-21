# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.find_height_and_balance(root)[1]
    def find_height_and_balance(self, root):
        if not root:
            return [0, True]
        
        left_height_and_balance = self.find_height_and_balance(root.left)
        right_height_and_balance = self.find_height_and_balance(root.right)

        balanced = left_height_and_balance[1] and right_height_and_balance[1] and abs(left_height_and_balance[0] - right_height_and_balance[0]) <= 1

        return (1+max(left_height_and_balance[0], right_height_and_balance[0]), balanced)