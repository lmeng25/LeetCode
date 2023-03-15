class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0 for i in range(len(s) + 1)]
        dp[-1] = 1
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word and dp[i + len(word)] == 1:
                    dp[i] = 1
                    break;
            
        return dp[0]