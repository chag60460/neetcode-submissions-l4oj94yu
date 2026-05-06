from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        left = 0
        right = len(self.hashmap[key]) - 1
        value = ""

        while left <= right:
            mid_point = (left + right) // 2 
            
            if self.hashmap[key][mid_point][0] <= timestamp:
                value = self.hashmap[key][mid_point][1]
                left = mid_point + 1
            else:
                right = mid_point - 1

        return value