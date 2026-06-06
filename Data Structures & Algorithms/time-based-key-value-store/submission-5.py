class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        left_index, right_index = 0, len(self.hashmap[key]) - 1
        value = ""

        while left_index <= right_index:
            midpoint_index = (left_index + right_index) // 2

            if self.hashmap[key][midpoint_index][0] > timestamp:
                right_index = midpoint_index - 1
            else:
                value = self.hashmap[key][midpoint_index][1]
                left_index = midpoint_index + 1
        
        return value