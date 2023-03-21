class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, subset):
            copy = list(subset)
            copy.sort()
            if copy not in res:
                res.append(copy)
            if i >= len(nums):
                return
            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j + 1, subset)
                subset.pop()
            
        dfs(0, [])
        return res