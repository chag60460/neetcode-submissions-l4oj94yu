# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        tracking_queue = collections.deque()
        tracking_queue.append(root)

        while tracking_queue:
            level_collection = []
            for i in range(len(tracking_queue)):
                node = tracking_queue.popleft()
                level_collection.append(node.val)
                if node.left:
                    tracking_queue.append(node.left)
                if node.right:
                    tracking_queue.append(node.right)
            output.append(level_collection)

        return output