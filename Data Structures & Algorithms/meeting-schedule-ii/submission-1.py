"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_start_time_array = sorted([interval.start for interval in intervals])
        sorted_end_time_array = sorted([interval.end for interval in intervals])

        count = 0
        max_count = 0

        start = 0
        end = 0

        while start < len(sorted_start_time_array):
            if sorted_start_time_array[start] < sorted_end_time_array[end]:
                count += 1
                start += 1
            else:
                count -= 1
                end += 1
            max_count = max(max_count, count)
        
        return max_count
