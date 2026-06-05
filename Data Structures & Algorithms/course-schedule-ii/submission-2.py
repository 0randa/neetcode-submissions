class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {n: [] for n in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        # create an output array and visit and cycle sets

        output, visit, cycle = [], set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)

            for pre in graph[crs]:
                if not dfs(pre): return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for n in range(numCourses):
            if not dfs(n): return []

        return output
        

    

            
