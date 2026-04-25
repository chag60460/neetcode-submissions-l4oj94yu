"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None}
        start = head
        
        while start:
            node = Node(start.val)
            hashmap[start] = node
            start = start.next
        
        start = head
        while start:
            node = hashmap[start]
            node.next = hashmap[start.next]
            node.random = hashmap[start.random]

            start = start.next
        
        return hashmap[head]