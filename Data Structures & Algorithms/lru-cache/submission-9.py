class DoubleLinkedListNode:
    def __init__(self, key: int, value: int, next=None, previous=None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_hashmap = {}

        self.lru_accessor = DoubleLinkedListNode(0,0)
        self.mru_accessor = DoubleLinkedListNode(0,0)

        self.lru_accessor.next = self.mru_accessor
        self.mru_accessor.previous = self.lru_accessor
        
    def get(self, key: int) -> int:
        if key in self.cache_hashmap:
            node = self.cache_hashmap[key]
            self._remove(node)
            self._add(node)
            return self.cache_hashmap[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_hashmap:
            self._remove(self.cache_hashmap[key])
            del self.cache_hashmap[key]
        
        if len(self.cache_hashmap) >= self.capacity:
            lru_node = self.lru_accessor.next
            self._remove(lru_node)
            del self.cache_hashmap[lru_node.key]
        
        new_node = DoubleLinkedListNode(key, value)
        self._add(new_node)
        self.cache_hashmap[key] = new_node

    def _remove(self, node):
        previous_node = node.previous
        next_node = node.next

        previous_node.next = next_node
        next_node.previous = previous_node

        #Optional cleanup
        node.previous = None
        node.next = None

    def _add(self, node):
        current_mru_node = self.mru_accessor.previous

        current_mru_node.next = node
        node.previous = current_mru_node

        node.next = self.mru_accessor
        self.mru_accessor.previous = node
