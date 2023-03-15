class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = 1
                    break
        
        return dp[-1]