class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters = { '2' : "abc",
                    '3' : "def",
                    '4' : "ghi",
                    '5' : "jkl",
                    '6' : "mno",
                    '7' : "pqrs",
                    '8' : "tuv",
                    '9' : "wxyz"}
        
        res = []
        def dfs(i, comb):
            if len(comb) == len(digits):
                res.append(comb)
            for j in range(i, len(digits)):
                currLetters = letters[digits[j]]
                for k in range(len(currLetters)):
                    comb += currLetters[k]
                    dfs(j + 1, comb)
                    comb = comb[:-1]
        
        dfs(0, "")
        return res
        