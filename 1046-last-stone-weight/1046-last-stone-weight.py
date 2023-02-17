class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            num1 = heapq.heappop(heap)
            if heap:
                num2 = heapq.heappop(heap)
                remain = abs(abs(num1) - abs(num2))
                if remain != 0:
                    heapq.heappush(heap, -1 * remain)
        return 0 if not heap else abs(heap[0])