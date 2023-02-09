class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def twoSum(i):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    temp = [nums[i], nums[l], nums[r]]
                    if temp not in res:
                        res.append(temp)
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            twoSum(i)
        
        return res