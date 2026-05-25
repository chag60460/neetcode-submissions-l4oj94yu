from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        current = root
        tracking_queue = deque([root])

        while tracking_queue:
            current_level = []

            for i in range(len(tracking_queue)):
                element = tracking_queue.popleft()
                if element:
                    current_level.append(element.val)
                    tracking_queue.append(element.left)
                    tracking_queue.append(element.right)

            if current_level:
                output.append(current_level)

        return output