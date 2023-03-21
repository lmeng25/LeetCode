class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        lastNum = 0
        
        def dfs(i, currSum, currList):
            nonlocal lastNum
            if currSum == target:
                res.append(list(currList))
            if currSum > target:
                return
            for j in range(i, len(candidates)):
                if candidates[j] == lastNum:
                    continue
                currList.append(candidates[j])
                currSum += candidates[j]
                dfs(j + 1, currSum, currList)
                lastNum = candidates[j]
                currList.pop()
                currSum -= candidates[j]
                
        dfs(0, 0, [])
        return res