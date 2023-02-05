from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] = map[num] + 1
            else:
                map[num] = 1
        
        sorted_list = sorted(map.items(), key = lambda item: item[1], reverse = True)
        first_k = sorted_list[:k]
        res = [item[0] for item in first_k]
        
        return res
        