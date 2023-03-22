class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(str):
            if len(str) == 1:
                return True
            l = 0
            r = len(str) - 1
            while l <= r:
                if str[l] != str[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(i, currList):
            if i >= len(s):
                res.append(currList.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    currList.append(s[i:j + 1])
                    dfs(j + 1, currList)
                    currList.pop()
                        
        dfs(0, [])
        return res
            