class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

        self.next = None
        self.previous = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.lru = ListNode(0,0)
        self.mru = ListNode(0,0)

        self.lru.next = self.mru
        self.mru.previous = self.lru

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])

        node = ListNode(key, value)
        self._add(node)
        self.hashmap[key] = node

        if len(self.hashmap) > self.capacity:
            lru_node = self.lru.next
            self._remove(lru_node)
            del self.hashmap[lru_node.key]

    
    def _remove(self, node: ListNode) -> None:
        previous_node = node.previous
        next_node = node.next

        previous_node.next = next_node
        next_node.previous = previous_node

    def _add(self, node: ListNode) -> None:
        previous_node = self.mru.previous
        previous_node.next = node
        node.previous = previous_node

        node.next = self.mru
        self.mru.previous = node