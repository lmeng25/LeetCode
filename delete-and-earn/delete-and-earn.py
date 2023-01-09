class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = {}
        memo = {}
        maxNum = 0
        for num in nums:
            if num in points:
                points[num] = points[num] + num
            else:
                points[num] = num
            maxNum = max(num, maxNum)
        
        def dp(num):
            if num == 0:
                return 0
            if num == 1:
                return points.get(1, 0)
            
            if num in memo:
                return memo[num]
            else:
                memo[num] = max(dp(num - 1), dp(num - 2) + points.get(num, 0))
                return memo[num]
          
        return dp(maxNum)
