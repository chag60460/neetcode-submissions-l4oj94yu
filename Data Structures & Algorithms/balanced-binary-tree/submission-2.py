# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.find_height(root)[0]

    def find_height(self, root):
        if not root:
            return [True, 0]
        
        left_tuple = self.find_height(root.left)
        right_tuple = self.find_height(root.right)

        balanced = left_tuple[0] and right_tuple[0] and abs(left_tuple[1] - right_tuple[1]) <= 1

        return (balanced, 1+max(left_tuple[1], right_tuple[1]))