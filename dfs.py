n = int(input("Enter number of nodes: "))

print("Enter adjacency matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]

start = int(input("Enter starting node: "))

visited = [False] * n

def dfs(u):
    visited[u] = True
    print(u, end=" ")

    # 🔑 traverse neighbors in REVERSE order
    for v in range(n-1, -1, -1):
        if graph[u][v] == 1 and not visited[v]:
            dfs(v)

print("DFS Traversal:", end=" ")
dfs(start)
