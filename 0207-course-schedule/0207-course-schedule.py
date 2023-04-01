class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        
        for pair in prerequisites:
            crs, pre = pair
            if crs in courses:
                courses[crs].append(pre)
            else:
                courses[crs] = [pre]

        visited = set()            
        def dfs(crs):
            if crs in visited:
                return False
            if crs not in courses:
                return True
            
            visited.add(crs)
            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            del courses[crs]
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True