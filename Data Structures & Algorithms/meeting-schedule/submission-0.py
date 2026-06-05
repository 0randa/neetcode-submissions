"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # iterate through all of the intervals, and check for the start and finish
        if len(intervals) == 1:
            return True


        prev = intervals[0]

        for i in intervals[1:]:
            # print(i)
            # start of current has to be greater than or equal to end of previous
            if not (i.start >= prev.end):
                return False


            prev = i

        return True
