class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        i = 0
        while i < len(s):
            # odd length
            k = i
            j = i + 1
            while k >= 0 and j < len(s):
                if s[k] == s[j]:
                    res += 1
                    k -= 1
                    j += 1
                else:
                    break

            # even length
            k = i
            j = i
            while k >= 0 and j < len(s):
                if s[k] == s[j]:
                    res += 1
                    k -= 1
                    j += 1
                else:
                    break

            i += 1

        return res