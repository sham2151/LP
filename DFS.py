class Solution:
    def dfs_algo(self, node, adj, visited, result):
        # Mark current node as visited
        visited[node] = 1
        result.append(node)

        # Visit all unvisited neighbors
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs_algo(neighbor, adj, visited, result)

    def dfs(self, adj):
        total_nodes = len(adj)
        visited = [0] * total_nodes
        result = []

        # Loop through all nodes (important for disconnected graph)
        for i in range(total_nodes):
            if not visited[i]:
                self.dfs_algo(i, adj, visited, result)

        return result


# --------- Example Usage ---------
if __name__ == "__main__":
    adj = [
        [1, 2],   # 0
        [0, 3],   # 1
        [0, 4],   # 2
        [1],      # 3
        [2]       # 4
    ]

    sol = Solution()
    print(sol.dfs(adj))