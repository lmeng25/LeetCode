class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[0] * n for _ in range(n)]
        res = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                memo[i][j] = s[i] == s[j] and (j - i + 1 <= 3 or memo[i + 1][j - 1])
                res += memo[i][j]
                    
        return res