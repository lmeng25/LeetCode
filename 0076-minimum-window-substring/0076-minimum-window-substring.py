class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(s) < len(t):
            return res
        
        # build a hashmap for the chars in t 
        hmap = {}
        for i in range(len(t)):
            if t[i] not in hmap:
                hmap[t[i]] = 1
            else:
                hmap[t[i]] += 1
        
        # window pointers and hashmap for the chars in the window && in t
        l = 0
        r = 0
        windowMap = {}
        windowCount = 0
        mapCount = len(hmap)

        while r < len(s):
            if s[r] not in hmap:
                r += 1
            else:
                windowMap[s[r]] = windowMap.get(s[r], 0) + 1
                if windowMap[s[r]] == hmap[s[r]]:
                    windowCount += 1

                while l <= r and windowCount == mapCount:
                    if res == "" or len(res) > (r - l + 1):
                        res = s[l:r+1]
                    if s[l] in hmap:
                        windowMap[s[l]] -= 1
                    if s[l] in hmap and windowMap[s[l]] < hmap[s[l]]:
                        windowCount -= 1
                    l += 1
                r += 1
            
        return res