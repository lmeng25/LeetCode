class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            k = target - nums[i]
            if k not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [i, hashmap[k]]
            