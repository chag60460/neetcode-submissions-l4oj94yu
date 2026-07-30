class DoubleLinkedNode:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity

        self.lru = DoubleLinkedNode(0,0)
        self.mru = DoubleLinkedNode(0,0)

        self.lru.next = self.mru
        self.mru.previous = self.lru

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]

            self._remove(node)
            self._add(node)
            
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
            del self.hashmap[key]
        
        if len(self.hashmap) >= self.capacity:
            lru = self.lru.next
            self._remove(lru)
            del self.hashmap[lru.key]
        
        node = DoubleLinkedNode(key, value)
        self._add(node)
        self.hashmap[key] = node
    
    def _remove(self, node):
        previous_node = node.previous
        next_node = node.next

        node.previous = None
        node.next = None

        previous_node.next = next_node
        next_node.previous = previous_node
    
    def _add(self, node):
        previous_mru = self.mru.previous

        previous_mru.next = node
        self.mru.previous = node

        node.next = self.mru
        node.previous = previous_mru