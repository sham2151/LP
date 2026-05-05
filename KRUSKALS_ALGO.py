class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False  # cycle detected

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return True


def kruskal_mst(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    ds = DisjointSet(n)

    mst = []
    total_cost = 0

    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_cost += w

        if len(mst) == n - 1:
            break

    return mst, total_cost


# Example
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, cost = kruskal_mst(4, edges)

print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} -- {v} weight: {w}")

print("Total Cost:", cost) 