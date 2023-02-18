class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = []
        for item in counter:
            freq = -counter[item]
            heapq.heappush(heap, (freq, item))
        
        max_freq = -heapq.heappop(heap)[0]
        idle = (max_freq - 1) * n
        
        while heap:
            freq = -heap[0][0]
            if idle > 0: 
                idle -= min(max_freq - 1, freq, idle)
                heapq.heappop(heap)    
            else:
                break
        return idle + len(tasks)
        