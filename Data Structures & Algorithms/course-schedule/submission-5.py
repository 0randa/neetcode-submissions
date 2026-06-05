class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the curr DFS patht
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            # Course has no prerequisites
            if preMap[crs] == []:
                return True

            visitSet.add(crs)

            # run dfs on its pre requisites
            for pre in preMap[crs]:
                if not dfs(pre): return False

            visitSet.remove(crs)
            # set it to an empty list, execute the above condition.
            preMap[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs): return False

        return True