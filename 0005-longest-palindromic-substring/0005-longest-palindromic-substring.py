class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        lenRes = 1
        
        i = 0
        while i < len(s):
            # odd length
            k = i
            j = i + 1
            while k >= 0 and j < len(s):
                if s[k] == s[j]:
                    if (j - k + 1) > lenRes:
                        res = s[k : j + 1]
                        lenRes = len(res)
                    k -= 1
                    j += 1
                else:
                    break

            # even length
            k = i
            j = i
            while k >= 0 and j < len(s):
                if s[k] == s[j]:
                    if (j - k + 1) > lenRes:
                        res = s[k : j + 1]
                        lenRes = len(res)
                    k -= 1
                    j += 1
                else:
                    break

            i += 1

        return res