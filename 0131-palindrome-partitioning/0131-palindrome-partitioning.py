class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, comb):
            if i >= len(s):
                res.append(comb.copy())
                return
            for j in range(i, len(s)):
                if palindrome(s[i : j + 1]):
                    comb.append(s[i : j + 1])
                    dfs(j + 1, comb)
                    comb.pop()
        
        def palindrome(string):
            l = 0
            r = len(string) - 1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        dfs(0, [])
        return res