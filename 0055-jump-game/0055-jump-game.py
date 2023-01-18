class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def jump(i):
            if nums[i] + i >= len(nums) - 1:
                return True
            if i >= len(nums) - 1:
                return True
            for j in range(i + 1, i + nums[i] + 1):
                if j not in memo:
                    if jump(j):
                        memo[i] = True
                        memo[j] = True
            if i not in memo:
                memo[i] = False
            return memo[i]
        return jump(0)