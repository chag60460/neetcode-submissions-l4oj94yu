class DoubleLinkedNode:
    def __init__(self, key: int, value: int, next=None, previous=None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_hashmap = {}

        self.lru_accessor = DoubleLinkedNode(0,0)
        self.mru_accessor = DoubleLinkedNode(0,0)

        self.lru_accessor.next = self.mru_accessor
        self.mru_accessor.previous = self.lru_accessor

    def get(self, key: int) -> int:
        if key in self.cache_hashmap:
            node = self.cache_hashmap[key]
            self._remove(node)
            self._add(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_hashmap:
            node = self.cache_hashmap[key]
            self._remove(node)
            del self.cache_hashmap[key]
        
        if len(self.cache_hashmap) >= self.capacity:
            lru_node = self.lru_accessor.next
            self._remove(lru_node)
            del self.cache_hashmap[lru_node.key]

        new_node = DoubleLinkedNode(key, value)
        self._add(new_node)
        self.cache_hashmap[key] = new_node

    def _remove(self, node):
        previous_node = node.previous
        next_node = node.next

        previous_node.next = next_node
        next_node.previous = previous_node

        #optional cleanup
        node.next = None
        node.previous = None

    def _add(self, node):
        mru_node = self.mru_accessor.previous

        mru_node.next = node
        node.previous = mru_node

        self.mru_accessor.previous = node
        node.next = self.mru_accessor
