class ListNode:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_hashmap = {}
        self.capacity = capacity

        self.mru = ListNode(0,0)
        self.lru = ListNode(0,0)

        self.mru.previous = self.lru
        self.lru.next = self.mru

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
            self._remove(self.cache_hashmap[key])
        
        node = ListNode(key, value)
        self._add(node)
        self.cache_hashmap[key] = node
        
        if len(self.cache_hashmap) > self.capacity:
            lru = self.lru.next
            self._remove(lru)
            del self.cache_hashmap[lru.key]

        
    def _add(self, node: ListNode):
        left_node = self.mru.previous

        left_node.next = node
        node.previous = left_node

        node.next = self.mru
        self.mru.previous = node
        
    def _remove(self, node: ListNode):
        left_node = node.previous
        right_node = node.next

        left_node.next = right_node
        right_node.previous = left_node
