class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[0] * n for _ in range(n)]
                
        maxLen = 0
        res = ""
        for i in range(n - 1, -1, -1):
            for j in range(i, len(s)):
                memo[i][j] = s[i] == s[j] and (j - i + 1 <= 3 or memo[i + 1][j - 1])
                if memo[i][j]:
                    if j - i + 1 <= maxLen:
                        continue
                    else:
                        res = s[i : j + 1]
                        maxLen = j - i + 1
        return res
            