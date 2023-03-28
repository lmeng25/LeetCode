class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(left, right, comb):
            if left + right == 2 * n:
                res.append(comb)
                return
            if left < n:
                comb += '('
                dfs(left + 1, right, comb)
                comb = comb[:-1]
            if right < n and right < left:
                comb += ')'
                dfs(left, right + 1, comb)
                comb = comb[:-1]
                
        dfs(0, 0, "")
        return res