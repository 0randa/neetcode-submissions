class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create an adjacency list
        graph = defaultdict(list)
        

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(i, parent, seen):
            if i in visited:
                return False

            visited.add(i)

            for neigh in graph[i]:
                if neigh == parent:
                    continue
                if not dfs(neigh, i, seen):
                    return False

            return True

        if not dfs(0, -1, set()):
            return False

        if len(visited) != n:
            return False

        return True