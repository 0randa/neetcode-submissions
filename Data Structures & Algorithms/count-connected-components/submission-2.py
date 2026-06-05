class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create an adjacency list

        adj_list = {i:[] for i in range(n)}
        visited = [False] * n
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)


        def dfs(node):
            for pre in adj_list[node]:
                if not visited[pre]:
                    visited[pre] = True
                    dfs(pre)

        num_comp = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                num_comp += 1
        return num_comp
