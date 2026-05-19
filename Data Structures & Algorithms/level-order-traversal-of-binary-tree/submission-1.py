# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        tracking_queue = collections.deque()
        tracking_queue.append(root)

        while tracking_queue:
            level_array = []
            length = len(tracking_queue)

            for i in range(length):
                node = tracking_queue.popleft()
                if node:
                    level_array.append(node.val)
                    tracking_queue.append(node.left)
                    tracking_queue.append(node.right)

            if level_array:
                output.append(level_array)
        
        return output
        