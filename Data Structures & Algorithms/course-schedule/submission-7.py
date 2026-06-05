class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        visited = [False] * numCourses

        def dfs(crs):
            if visited[crs]:
                return False
            if not graph[crs]:
                return True
            
            # chuck it into the set
            visited[crs] = True
            for pre in graph[crs]:
                if not dfs(pre): 
                    return False
            # remove it from the set
            visited[crs] = False
            return True


        for i in range(numCourses):
            if not dfs(i): 
                return False
        return True

        