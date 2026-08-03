class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list) #{key: [(timestamp1, value1), (timestamp2, value2)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
    
        value_array = self.hashmap[key]
        left = 0
        right = len(value_array) - 1
        value = ""

        while left <= right:
            midpoint = (left + right) // 2

            if value_array[midpoint][0] > timestamp:
                right = midpoint - 1
            else:
                value = value_array[midpoint][1]
                left = midpoint + 1

        return value
