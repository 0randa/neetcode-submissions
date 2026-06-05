class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfsHasCycle(G, v, visited, onStack):
            visited[v] = True
            onStack[v] = True

            for w,v in G:
                if onStack[w]:
                    return True
                elif not visited[w]:
                    if dfsHasCycle(G, w, visited, onStack):
                        return True
            
            onStack[v] = False
            return False



        def hasCycle(G):
            visited = [False] * numCourses
            onStack = [False] * numCourses


            for _, v in G:

                
                if dfsHasCycle(G, v, visited, onStack):
                    return True

            return False

        res = hasCycle(prerequisites)
        return not res