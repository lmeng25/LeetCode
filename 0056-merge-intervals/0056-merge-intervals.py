class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        
        i = 0
        curr = intervals[0]
        while i < len(intervals) - 1:
            curr = intervals[i]
            next = intervals[i + 1]
            if curr[1] >= next[0]:
                curr[1] = max(curr[1], next[1])
                intervals.pop(i + 1)
            else:
                i += 1
        return intervals
        