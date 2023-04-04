class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMap = {crs : [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            if crs in crsMap:
                crsMap[crs].append(pre)
            else:
                crsMap[crs] = [pre]
        
        cycle = set()
        visited = set()
        res = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res