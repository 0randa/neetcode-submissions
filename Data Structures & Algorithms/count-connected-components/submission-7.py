class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # approach: let's design a parent array, each index will represent a node, and it's element will be its parent.
        # n=3
        # edges=[[1,0],[2,1]]

        # 0 -> 1, 0 -> 2
                # then we use disjoint union set
        def find(x):
            while x != parent[x]:
                # change the current guy's parent to the parent's parent
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        parent = list(range(n))

        for u, v in edges:
            parent[find(v)] = find(u)

        print(parent)


        connected = set()

        for i in range(n):
            connected.add(find(i))

        return len(connected)
