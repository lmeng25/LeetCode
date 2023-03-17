class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(0, currSum)
            currSum += nums[i]
            maxSum = max(maxSum, currSum)

        minSum = nums[0]
        currSum = nums[0]
        for i in range(1, len(nums)):
            currSum = min(0, currSum)
            currSum += nums[i]
            minSum = min(minSum, currSum)

        if sum(nums) == minSum:
            return maxSum
        return max(maxSum, sum(nums) - minSum)
        