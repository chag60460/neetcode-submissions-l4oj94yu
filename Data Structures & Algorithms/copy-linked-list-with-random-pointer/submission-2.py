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
            copy_node = Node(start.val)
            hashmap[start] = copy_node
            start = start.next
        
        start = head
        while start:
            hashmap[start].next = hashmap[start.next]
            hashmap[start].random = hashmap[start.random]
            start = start.next

        return hashmap[head]