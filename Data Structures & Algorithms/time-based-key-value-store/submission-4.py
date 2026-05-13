class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        left, right = 0, len(self.hashmap[key]) - 1
        value = ""

        while left <= right:

            midpoint = (left + right) // 2

            if self.hashmap[key][midpoint][0] > timestamp:
                right = midpoint - 1
            else:
                value = self.hashmap[key][midpoint][1]
                left = midpoint + 1
        
        return value