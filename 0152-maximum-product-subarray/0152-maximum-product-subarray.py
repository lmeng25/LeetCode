class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = min_so_far = res = nums[0]
        for i in range(1, len(nums)):
            temp = max_so_far
            max_so_far = max(max_so_far * nums[i], min_so_far * nums[i], nums[i])
            min_so_far = min(temp * nums[i], min_so_far * nums[i], nums[i])
            res = max(max_so_far, res)
        return res