class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        record = [0] * (pow(10, 6) + 1)
        
        for interval in intervals:
            for i in range(interval[0], interval[1]):
                if record[i] == 1:
                    return False
                else:
                    record[i] = 1
        
        return True