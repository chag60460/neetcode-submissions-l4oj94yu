class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        results = [sorted_intervals[0]]

        for interval in sorted_intervals:
            if results[-1][1] >= interval[0]:
                results[-1][1] = max(results[-1][1], interval[1])
            else:
                results.append(interval)
        
        return results

