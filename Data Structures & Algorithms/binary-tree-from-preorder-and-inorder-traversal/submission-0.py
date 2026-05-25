# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        rootNode = TreeNode(preorder[0])
        rootNodeMidpoint = inorder.index(preorder[0]) #this acts as a split point, telling us how many nodes are in the left and right

        #for pre-order list, after the root node, rootNodeMidpoint number of nodes in the left tree
        rootNode.left = self.buildTree(preorder[1:rootNodeMidpoint + 1], inorder[:rootNodeMidpoint])
        rootNode.right = self.buildTree(preorder[rootNodeMidpoint + 1:], inorder[rootNodeMidpoint + 1:])

        return rootNode