class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # let's create an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # we run DFS

        seen = set()

        num_comp = 0

        def dfs(i):
            if i in seen:
                return

            seen.add(i)
            for neigh in graph[i]:
                dfs(neigh)

        for i in range(n):
            if i in seen:
                continue
            
            dfs(i)
            num_comp += 1

        return num_comp