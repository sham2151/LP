import heapq

def spanningTree(V, adj):
    mst = []
    Sum = 0
    vis = [0] * V
    priority_queue = []

    heapq.heappush(priority_queue, (0, 0, -1))  # (wt, node, parent)

    while priority_queue:
        wt, node, parent = heapq.heappop(priority_queue)

        if vis[node] == 0:
            vis[node] = 1

            if parent != -1:
                Sum += wt
                mst.append((parent, node))

            for adjNode, wtt in adj[node]:
                if vis[adjNode] == 0:
                    heapq.heappush(priority_queue, (wtt, adjNode, node))

    return Sum, mst


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    V = 5
    adj = [
        [(1, 2), (3, 6)],              # 0
        [(0, 2), (2, 3), (3, 8), (4, 5)],  # 1
        [(1, 3), (4, 7)],              # 2
        [(0, 6), (1, 8)],              # 3
        [(1, 5), (2, 7)]               # 4
    ]

    Sum, mst = spanningTree(V, adj)

    print("MST Edges:")
    for u, v in mst:
        print(u, "-", v)

    print("Total Weight:", Sum)