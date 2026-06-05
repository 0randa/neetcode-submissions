class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = [False] * n
        
        
        for edge in edges:
            parent, child = edge

            if visited[child]:
                return False

            visited[child] = True

        return True