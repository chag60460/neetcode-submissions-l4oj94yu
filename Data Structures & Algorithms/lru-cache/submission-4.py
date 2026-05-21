class twoEndListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        #dummy nodes that allow us easy access
        self.mru = twoEndListNode(0,0)
        self.lru = twoEndListNode(0,0)

        self.lru.next = self.mru
        self.mru.prev = self.lru
        

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        
        node = twoEndListNode(key, value)
        self._add(node)
        self.hashmap[key] = node

        if len(self.hashmap) > self.capacity:
            lru_node = self.lru.next
            self._remove(lru_node)
            del self.hashmap[lru_node.key]
        
    def _remove(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node
    
    def _add(self, node):
        previous_node = self.mru.prev
        
        previous_node.next = node
        node.prev = previous_node

        node.next = self.mru
        self.mru.prev = node