class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap = {}
        for item in prerequisites:
            crs = item[0]
            pre = item[1]
            if crs in crsMap:
                crsMap[crs].append(pre)
            else:
                crsMap[crs] = [pre]
            
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if crs not in crsMap:
                return True
            
            visited.add(crs)
            for preCrs in crsMap[crs]:
                if not dfs(preCrs):
                    return False
            del crsMap[crs]
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True