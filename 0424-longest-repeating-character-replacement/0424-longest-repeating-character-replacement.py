class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        l = 0
        r = 1
        
        hmap = {}
        hmap[s[0]] = 1
        
        while r < len(s):
            if s[r] not in hmap:
                hmap[s[r]] = 1
            else:
                hmap[s[r]] += 1
            max_count = max(hmap.values())
            length = r - l + 1
            need_replace = length - max_count
            
            if need_replace <= k:
                res = max(res, length)
                r += 1
            else:
                hmap[s[l]] -= 1
                l += 1
                r += 1
        
        return res