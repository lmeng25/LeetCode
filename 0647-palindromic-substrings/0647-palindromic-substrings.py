class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        def dp(i, j):
            if j - i + 1 <= 3:
                return s[i] == s[j]
            
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                if s[i] != s[j]:
                    memo[(i, j)] = False
                    return False
                else:
                    memo[(i, j)] = dp(i + 1, j - 1)
                return memo[(i, j)]
        
        res = 0
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if dp(i, j):
                    res += 1
                    
        return res