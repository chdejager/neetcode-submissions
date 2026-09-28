"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()

        s = 0
        e = 0
        rooms = 0
        max_rooms = 0

        while s < len(starts):
            if starts[s] < ends[e]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1
        
        return max_rooms




