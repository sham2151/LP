import heapq

class Solution:
    # A* Algorithm
    def astar(self, v, edges, h, start, goal):
        
        # Step 1: Create adjacency list
        adj_list = [[] for _ in range(v)]
        for u, vtx, wt in edges:
            adj_list[u].append((vtx, wt))
            adj_list[vtx].append((u, wt))   # remove if directed

        # Step 2: Distance (g(n))
        dist = [float("inf")] * v
        dist[start] = 0

        # Step 3: Parent (for path)
        parent = [-1] * v

        # Step 4: Min heap (f(n), node)
        pq = []
        heapq.heappush(pq, (h[start], start))

        while pq:
            fn, node = heapq.heappop(pq)

            # Stop when goal reached
            if node == goal:
                break

            # Skip outdated entries
            if fn > dist[node] + h[node]:
                continue

            # Explore neighbors
            for adjNode, weight in adj_list[node]:
                gn = dist[node] + weight

                if gn < dist[adjNode]:
                    dist[adjNode] = gn
                    fn = gn + h[adjNode]
                    heapq.heappush(pq, (fn, adjNode))
                    parent[adjNode] = node

        return dist, parent


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    V = 4

    edges = [
        (0, 1, 1),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 5),
        (2, 3, 3)
    ]

    # Heuristic values
    h = [4, 1, 2, 0]

    start = 0
    goal = 3

    sol = Solution()
    dist, parent = sol.astar(V, edges, h, start, goal)

    print("Distance:", dist)
    print("Parent:", parent)

    # Path reconstruction
    path = []
    node = goal
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()

    print("Path:", path)