class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(numRows):
            rows = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    rows.append(1)
                else:
                    rows.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(rows)
        
        return res