import heapq

class Solution:
    # Function to find shortest distances from src to all vertices
    def dijkstra(self, v, edges, src):
        
        # Step 1: Create adjacency list
        adj_list = [[] for _ in range(v)]
        for u, v2, wt in edges:
            adj_list[u].append((v2, wt))
            adj_list[v2].append((u, wt))   # remove this line if graph is directed

        # Step 2: Initialize distance array
        distance = [float("inf")] * v
        distance[src] = 0

        # Step 3: Min heap (priority queue)
        priority_queue = []
        heapq.heappush(priority_queue, (0, src))   # (distance, node)

        # Step 4: Dijkstra (Greedy)
        while priority_queue:
            curr_dist, node = heapq.heappop(priority_queue)

            # Skip outdated entries
            if curr_dist > distance[node]:
                continue

            # Explore neighbors
            for adjNode, weight in adj_list[node]:
                new_dist = curr_dist + weight

                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist
                    heapq.heappush(priority_queue, (new_dist, adjNode))

        return distance


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    V = 5

    # edges = (u, v, weight)
    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7)
    ]

    src = 0

    sol = Solution()
    result = sol.dijkstra(V, edges, src)

    print("Shortest distances from source", src)
    for i in range(V):
        print(f"{src} -> {i} = {result[i]}")