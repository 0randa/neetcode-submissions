class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        # minimum spanning tree?
        def find(n):
            # find the most common ancestor
            p = par[n]
            while p != par[n]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(n1, n2):
            # find the ancestor of both n1 and n2.
            p1, p2 = find(n1), find(n2)

            # if they have the same ancestor, then ???
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

            

                
