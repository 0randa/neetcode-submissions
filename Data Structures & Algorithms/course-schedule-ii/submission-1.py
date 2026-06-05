class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {n: [] for n in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)


        # we can chuck all of the subjects with no prereqs into this
        q = deque()
        visited = set()
        res = []

        for n in range(numCourses):
            if not graph[n]:
                q.append(n)


        while q:
            node = q.popleft()
            if node in visited:
                return []
  
            res.append(node)

            # find all the nodes in which node is a prereq of
            for n in range(numCourses):
                if node in graph[n]:
                    q.append(n)

        return res

            
