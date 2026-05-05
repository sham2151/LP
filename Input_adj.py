v = int(input("Enter the number of vertices:"))
e = int(input("Enter the number of edges:"))

adj = [[] for _ in range(v)]

for _ in range(e):
    u,v,w = map(int,input().split())

    adj[u].append((v,w))
    adj[v].append((u,w))

print(adj)