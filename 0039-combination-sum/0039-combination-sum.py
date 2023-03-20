class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(i, currSum, currList):
            if target == currSum:
                res.append(list(currList))
                return
            if target < currSum:
                return
            for j in range(i, len(candidates)):
                currList.append(candidates[j])
                currSum += candidates[j]
                dfs(j, currSum, currList)
                currList.pop()
                currSum -= candidates[j]
                
        dfs(0, 0, [])
        return res
            