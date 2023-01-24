class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        
        i = 0
        j = 1
        while j < len(intervals):
            curr = intervals[i]
            next = intervals[j]
            if curr[1] <= next[0]:
                i = j
                j += 1
            elif curr[1] > next[1]:
                i = j
                j += 1
                res += 1
            else:
                j += 1
                res += 1
                
        return res
            
            