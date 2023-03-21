class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(perm, arr):
            if len(perm) == len(nums):
                res.append(list(perm))
                return
            for j in arr:
                tPerm = list(perm)
                tArr = list(arr)
                tPerm.append(j)
                tArr.remove(j)
                dfs(tPerm, tArr)
        
        dfs([], nums)
        return res