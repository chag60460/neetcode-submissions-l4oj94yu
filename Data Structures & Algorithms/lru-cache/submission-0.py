class ListNode:

    def __init__(self, key: int, val:int):
        self.key = key
        self.val = val

        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)

        self.head.next = self.tail
        self.tail.previous = self.head
    
    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            old_node = self.hashmap[key]
            self._remove(old_node)
        
        new_node = ListNode(key, value)
        self._add(new_node)
        self.hashmap[key] = new_node

        if len(self.hashmap) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.hashmap[lru.key]
    
    def _add(self, node:ListNode):
        left_node = self.tail.previous
        
        left_node.next = node
        self.tail.previous = node

        node.previous = left_node
        node.next = self.tail
    
    def _remove(self, node:ListNode):
        left_node = node.previous
        right_node = node.next

        left_node.next = right_node
        right_node.previous = left_node

