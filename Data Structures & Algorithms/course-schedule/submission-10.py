class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # we should create an adjacency list first
        if not prerequisites:
            return True

        adj_list = {i: [] for i in range(numCourses)}
        
        for course, prer in prerequisites:
            adj_list[course].append(prer)
            
        # I think we should have some dfs/bfs algorithm

        # 

        seen = set()

        def dfs(node):
            if node in seen:
                return False
            
            # no prerequisites
            if adj_list[node] == []:
                return True

            seen.add(node)

            for pre in adj_list[node]:
                if not dfs(pre):
                    return False

            seen.remove(node)
            adj_list[node] = []
            return True
            
        
        for i in range(numCourses):
            # return False if the list is too long, or there's a cycle, or there's just not 
            if not dfs(i):
                return False
        return True