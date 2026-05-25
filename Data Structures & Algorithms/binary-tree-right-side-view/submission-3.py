from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ouptut = []
        tracking_queue = deque([root])

        while tracking_queue:
            rightmost_node = None

            for _ in range(len(tracking_queue)):
                node = tracking_queue.popleft()
                if node:
                    rightmost_node = node
                    tracking_queue.append(node.left)
                    tracking_queue.append(node.right)
            
            if rightmost_node:
                ouptut.append(rightmost_node.val)
        
        return ouptut