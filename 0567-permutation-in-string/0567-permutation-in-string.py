class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for i in range(len(s1)):
            if s1[i] not in hmap:
                hmap[s1[i]] = 1
            else:
                hmap[s1[i]] += 1
        
        l = 0
        r = 0
        while r < len(s2):
            if s2[r] not in hmap:
                while l < r:
                    hmap[s2[l]] += 1
                    l += 1
                r = r + 1
                l = r
            elif hmap[s2[r]] == 0:
                while True:
                    hmap[s2[l]] += 1
                    l += 1
                    if hmap[s2[r]] == 1:
                        break;
            else:
                hmap[s2[r]] -= 1
                r += 1
                if max(hmap.values()) == 0:
                    return True
        
        return False