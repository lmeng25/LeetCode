class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = { 0 : 1}
        prefix_sum = 0
        res = 0
        
        for n in nums:
            prefix_sum += n
            reminder = prefix_sum % k
            res += freq.get(reminder, 0)
            freq[reminder] = freq.get(reminder, 0) + 1
        
        return res