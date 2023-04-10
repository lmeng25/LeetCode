class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        l = 0
        r = nums[0]
        
        res = 1
        while r < len(nums) - 1:
            temp = r
            res += 1
            for i in range(l, r + 1):
                r = max(r, i + nums[i])
                if r >= len(nums) - 1:
                    return res
            l = temp + 1
        return res