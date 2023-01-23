class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        # insert new interval to the list
        inserted = False
        for i in range(len(intervals)):
            if newInterval < intervals[i]:
                intervals.insert(i, newInterval)
                inserted = True
                break
        
        if not inserted:
            intervals.append(newInterval)
        
        # iterate the list and merge overlaps
        i = 0
        curr = intervals[0]
        for i in range(len(intervals) - 1):
            curr = intervals[i]
            next = intervals[i + 1]
            if curr[1] >= next[0]:
                curr[1] = max(next[1], curr[1])
                intervals.pop(i + 1)
                break
        i += 1
        while i < len(intervals):
            next = intervals[i]
            if curr[1] < next[0]:
                break
            else:
                if curr[1] <= next[1]:
                    curr[1] = next[1]
                intervals.pop(i)
        return intervals