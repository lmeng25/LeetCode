class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def jump(i):
            if i >= len(nums) - 1:
                return True
            # if nums[i] == 0:
            #     return False
            for j in range(i + 1, i + nums[i] + 1):
                if j not in memo:
                    if jump(j):
                        memo[j] = True
                        return True
            if i not in memo:
                memo[i] = False
            return memo[i]
        return jump(0)