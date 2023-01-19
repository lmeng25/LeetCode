from queue import PriorityQueue
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = PriorityQueue()
        
        for meeting in intervals:
            if rooms.qsize() != 0:
                if rooms.queue[0] <= meeting[0]:
                    rooms.get()
            rooms.put(meeting[1], meeting[1])
        
        return rooms.qsize()