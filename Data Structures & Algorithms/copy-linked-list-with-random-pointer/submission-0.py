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
        original_to_copy_hashmap = {None:None}

        start = head
        while start:
            original_to_copy_hashmap[start] = Node(start.val)
            start = start.next
        
        start_again = head
        while start_again:
            original_to_copy_hashmap[start_again].next = original_to_copy_hashmap[start_again.next]
            original_to_copy_hashmap[start_again].random = original_to_copy_hashmap[start_again.random]
            start_again = start_again.next
        
        return original_to_copy_hashmap[head]