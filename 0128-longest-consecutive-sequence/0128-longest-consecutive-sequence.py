class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        heapq.heapify(nums)
        
        while len(nums) != 0:
            temp = heapq.heappop(nums)
            length = 1
            while len(nums) != 0:
                if nums[0] - temp > 1:
                    break
                if nums[0] - temp == 1:
                    length += 1
                temp = heapq.heappop(nums)
            res = max(res, length)
        
        return res
            