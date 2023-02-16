class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = { 0 : 1}
        prefix_sum = 0
        res = 0
        for n in nums:
            prefix_sum += n
            res += freq.get(prefix_sum - k, 0)
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        
        return res