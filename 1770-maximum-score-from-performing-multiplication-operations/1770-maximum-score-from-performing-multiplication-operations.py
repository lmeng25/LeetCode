class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        if len(multipliers) == 0:
            return 0

        memo = {}
        def dp(i, left):
            if i >= len(multipliers):
                return 0
            right = len(nums) - 1 - (i - left)
            if (i, left) in memo:
                return memo[(i, left)]
            else:
                memo[(i, left)] = max(dp(i + 1, left + 1) + multipliers[i] * nums[left]
                                      , dp(i + 1, left) + multipliers[i] * nums[right])
                return memo[(i, left)]
        
        return dp(0, 0)