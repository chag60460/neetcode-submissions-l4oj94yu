# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root

        while current:
            if not current.left: #it is the leftmost node - visit it directly, then proceed inorder traversal
                k -= 1
                if k == 0:
                    return current.val
                else:
                    current = current.right
            else: #if it has a left child - inorder traversal
                
                #the following is to keep track of nodes we've visited without a stack

                #find the rightmost node of the left tree
                left_tree_rightmost = current.left
                while left_tree_rightmost.right and left_tree_rightmost.right != current:
                    left_tree_rightmost = left_tree_rightmost.right
                
                if not left_tree_rightmost.right: #parent hasn't been linked, so we want to do that first
                    #link current node to left_tree_rightmost, so we visit in that order (next outer while loop)
                    left_tree_rightmost.right = current
                    #move current to left
                    current = current.left
                else: #Parent is already marked, we can go ahead and traverse that node
                    left_tree_rightmost.right = None
                    k -= 1
                    if k == 0:
                        return current.val
                    current = current.right
        
        return -1