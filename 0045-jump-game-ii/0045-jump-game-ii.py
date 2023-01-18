class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = 0
        r = 0
        
        while r < len(nums) - 1:
            farmost = r
            for i in range(l, r + 1):
                farmost = max(farmost, i + nums[i])
            l = r + 1
            r = farmost
            res += 1
            
        return res
            
            