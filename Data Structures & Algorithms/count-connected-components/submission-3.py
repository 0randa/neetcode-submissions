class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create an adjacency list
        graph = {i:[] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)
        num_comp = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                num_comp += 1

        return num_comp
