import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # first we form an adjacency list

        # format:
        # u: (v, weight)

        # output a dictionary where we have n and then the weight
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v,w))


        pq = []

        heapq.heappush(pq, (0, src))

        visited = {}

        while pq:
            p, item = heapq.heappop(pq)

            if item in visited:
                continue

            visited[item] = p
            # weights[item] = p

            print(p, item)
            for neigh in graph[item]:
                node, weight = neigh

                if node in visited:
                    continue

                # new weight will be p + weight
                # which is the weight from src to new_w
                new_w = p + weight
                heapq.heappush(pq, (new_w, node))

        # print(weights)
        for i in range(n):
            if i not in visited:
                visited[i] = -1

        return visited

