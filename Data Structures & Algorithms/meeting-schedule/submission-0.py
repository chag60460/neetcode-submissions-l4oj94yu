"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_array = sorted(intervals, key= lambda interval: interval.start)
        i = 0

        while i < len(sorted_array) - 1:
            if sorted_array[i].end > sorted_array[i+1].start:
                return False
            i += 1
        
        return True