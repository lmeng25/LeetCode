class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:
                return 1
            
            if i not in memo:
                if int(s[i:i+2]) <= 26:
                    memo[i] = dp(i + 1) + dp(i + 2)
                else:
                    memo[i] = dp(i + 1)
            
            return memo[i]
        
        return dp(0)
                