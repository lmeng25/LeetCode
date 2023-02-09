class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        to_left = [1] * n
        to_right = [1] * n
        
        for i in range(n - 2, -1, -1):
            to_left[i] = to_left[i + 1] * nums[i + 1]
        
        for i in range(1, n, 1):
            to_right[i] = to_right[i - 1] * nums[i - 1]
            
        for i in range(n):
            res.append(to_left[i] * to_right[i])
            
        return res