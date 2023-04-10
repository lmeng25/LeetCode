class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        max_cumu = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            max_cumu = max(n, max_cumu + n)
            res = max(res, max_cumu)
        
        return res