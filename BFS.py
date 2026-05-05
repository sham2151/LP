from collections import deque

class Solution:
    def bfs_algo(self, n, adj, start):
        ans = []
        visited = [0] * n
        queue = deque([start])
        visited[start] = 1

        while queue:
            u = queue.popleft()
            ans.append(u)

            for v in adj[u]:
                if visited[v] == 0:
                    visited[v] = 1
                    queue.append(v)

        return ans

    def bfs(self, adj):
        n = len(adj)
        return self.bfs_algo(n, adj, 0)


# 🔹 Driver Code (IMPORTANT FOR EXAM)
adj = [
    [1, 2],
    [0, 3],
    [0, 4],
    [1],
    [2]
]

sol = Solution()
print("BFS Traversal:", sol.bfs(adj))