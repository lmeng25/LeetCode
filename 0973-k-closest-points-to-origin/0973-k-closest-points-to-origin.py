class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        
        for point in points:
            dist = (point[0] ** 2 + point[1] ** 2) ** (1 / 2)
            heapq.heappush(heap, (dist, point))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res