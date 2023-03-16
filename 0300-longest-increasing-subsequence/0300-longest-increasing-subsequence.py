class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, - 1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
        return res
        