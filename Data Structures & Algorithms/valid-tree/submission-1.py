class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def create_list():
            adjacency_list = {}
            for i in range(n):
                adjacency_list[i] = []

            for u,v in edges:
                adjacency_list[v].append(u)
                adjacency_list[u].append(v)

            return adjacency_list

        adj_list = create_list()

        def dfsHasCycle(G, v, prev, visited):
            visited[v] = True

            for w in adj_list[v]:
                if w == prev:
                    continue
                if visited[w]:
                    return True
                elif dfsHasCycle(G, w, v, visited):
                    return True

            return False
                
        def hasCycle(G):
            visited = [False] * n

            for v in range(n):
                if not visited[v]:
                    if dfsHasCycle(G, v, v, visited):
                        return True
            return False
        
        ans = hasCycle(adj_list)

        return (not ans)