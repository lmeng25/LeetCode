class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l = 0
        r = 1
        res = 1
        
        hmap = {}
        hmap[s[l]] = l
        
        while r < len(s):
            if s[r] in hmap:
                new_l = hmap[s[r]] + 1
                for i in range(l, new_l):
                    del hmap[s[i]]
                l = new_l
                hmap[s[r]] = r
                r += 1
            else:
                hmap[s[r]] = r
                res = max(res, r - l + 1)
                r += 1
        
        return res