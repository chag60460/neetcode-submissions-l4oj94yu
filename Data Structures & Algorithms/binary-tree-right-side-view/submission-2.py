# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        tracking_queue = deque([root])

        while tracking_queue:
            rightmost_node = None
            level_length = len(tracking_queue)
            
            while level_length:
                node = tracking_queue.popleft()
                if node:
                    rightmost_node = node
                    tracking_queue.append(node.left)
                    tracking_queue.append(node.right)
                level_length -= 1
            
            if rightmost_node:
                output.append(rightmost_node.val)
        
        return output