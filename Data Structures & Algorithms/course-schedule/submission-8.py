class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # we should create an adjacency list first

        adj_list = {}

        
        for course, prer in prerequisites:
            adj_list[course] = prer
            

        print(adj_list)


        # I think we should have some dfs/bfs algorithm

        # 
        def dfs(node, i):
            nonlocal seen
            if i >= numCourses:
                return False

            if node in seen:
                return False

            if node not in adj_list and i == numCourses - 1:
                return True

            seen.add(node)

            # 
            return dfs(adj_list[node], i + 1)
            
        
        for i in range(numCourses):
            # return False if the list is too long, or there's a cycle, or there's just not 
            seen = set()
            if dfs(i, 1):
                return True
        return False