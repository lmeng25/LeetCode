class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def twoSum(i):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i - 1]:
                twoSum(i)
        
        return res