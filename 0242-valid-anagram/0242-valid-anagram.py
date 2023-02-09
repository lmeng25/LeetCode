class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in hashmap or hashmap[t[i]] == 0:
                return False
            else:
                hashmap[t[i]] -= 1
        
        for count in hashmap.values():
            if count != 0:
                return False
            
        return True