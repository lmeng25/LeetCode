class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j - i + 1 <= 3:
                    memo[(i, j)] = s[i] == s[j]     
                else:
                    if s[i] != s[j]:
                        memo[(i, j)] = False
                        return False
                    else:
                        memo[(i, j)] = dp(i + 1, j - 1)
            return memo[(i, j)]
        
        res = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if dp(i, j):
                    res += 1
                    
        return res