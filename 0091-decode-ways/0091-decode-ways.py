class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        p1 = 1
        p2 = 1
        for i in range(2, len(s) + 1):
            res = 0
            if int(s[i - 1]) != 0:
                res = p2
            if 10 <= int(s[i - 2 : i]) <= 26:
                res += p1
            p1 = p2
            p2 = res
        
        return p2