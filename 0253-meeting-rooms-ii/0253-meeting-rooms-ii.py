import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        
        for meeting in intervals:
            if len(rooms) != 0:
                if rooms[0] <= meeting[0]:
                    heapq.heappop(rooms)
            heapq.heappush(rooms, meeting[1])
        
        return len(rooms)