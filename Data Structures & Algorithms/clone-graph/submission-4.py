"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # base cases
        if not node:
            return node
        if not node.neighbors:
            return Node()
        
        
        nodes = {

        }

        def dfs(node):
            if not node:
                return

            # debugging
            # print(node.val)

            for neighbour in node.neighbors:
                if neighbour.val not in nodes.keys():
                    print(neighbour)
                    nodes[neighbour.val] = {'val': neighbour.val, 'neighbours': [neigh.val for neigh in neighbour.neighbors]}
                    dfs(neighbour)

        dfs(node)
        # print(nodes)
        for i in range(1, len(nodes) + 1):
            nodes[i] = nodes[i] | {'node': Node(i)}

        # debugging
        # print(nodes)
        # add neighbours

        for i in range(1, len(nodes) + 1):
            for j in nodes[i]['neighbours']:
                nodes[i]['node'].neighbors.append(nodes[j]['node'])

        return nodes[1]['node']


