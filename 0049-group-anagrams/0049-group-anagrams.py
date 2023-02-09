class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for s in strs:
            char_arr = list(s)
            char_arr.sort()
            sorted_s = "".join(char_arr)
            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]
        
        return hashmap.values()