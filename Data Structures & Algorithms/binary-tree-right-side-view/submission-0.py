# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue = deque([root])

        while queue:
            rightmost_node = None
            queue_length = len(queue)

            while queue_length:
                node = queue.popleft()
                
                if node:
                    rightmost_node = node
                    queue.append(node.left)
                    queue.append(node.right)
                
                queue_length -= 1
        
            if rightmost_node:
                output.append(rightmost_node.val)
        
        return output