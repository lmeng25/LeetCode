class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i = 0
        j = 0
        left = 0
        right = len(matrix[0])
        up = 0
        bottom = len(matrix)
        
        while len(res) < len(matrix) * len(matrix[0]):
            while j < right:
                res.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            up += 1
            if not len(res) < len(matrix) * len(matrix[0]):
                break
                
            while i < bottom:
                res.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            right -= 1
            if not len(res) < len(matrix) * len(matrix[0]):
                break
                
            while j >= left:
                res.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            bottom -= 1
            if not len(res) < len(matrix) * len(matrix[0]):
                break;
                
            while i >= up:
                res.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            left += 1
        
        return res
            