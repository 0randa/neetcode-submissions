"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # find the longest chains.

        # we sort by the start time

        # then we utilise some kind of min heap

        intervals.sort(key = lambda x: x.start)

        if not intervals:
            return 0
        pq = [(intervals[0].end, None)]


        for i in intervals[1:]:

            # check that the start time does not conflict with the earliest end time
            earliest_end, _ = pq[0]

            if i.start >= earliest_end:
                heapq.heappop(pq)
            heapq.heappush(pq, (i.end, None))
            
        return len(pq)
