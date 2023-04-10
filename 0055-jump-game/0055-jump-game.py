class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        l = 0
        r = nums[0]
        
        while r < len(nums):
            temp = r
            for i in range(l, r + 1):
                r = max(r, nums[i] + i)
            if r >= len(nums) - 1:
                return True
            l = temp
            if l == r and nums[l] == 0:
                return False
            l += 1
        
        return True