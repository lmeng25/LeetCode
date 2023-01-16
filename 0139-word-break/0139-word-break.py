class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(i):
            if i > len(s) - 1:
                return True
            if i not in memo:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        if dp(j):
                            memo[i] = True
                            return True
                memo[i] = False
            return memo[i]
        
        return dp(0)
                    
            
            