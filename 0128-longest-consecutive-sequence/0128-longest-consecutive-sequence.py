class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)
        
        for n in hashset:
            if n - 1 not in hashset:
                curr = n
                count = 1
                while curr + 1 in hashset:
                    curr += 1
                    count += 1
                res = max(count, res)
        
        return res
            