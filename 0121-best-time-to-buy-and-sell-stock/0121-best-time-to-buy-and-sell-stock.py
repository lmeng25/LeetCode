class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
        
        return res