from collections import deque

n = int(input("Enter number of nodes: "))

print("Enter adjacency matrix:")
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting node: "))

visited = [False] * n
queue = deque([start])

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()

    if not visited[node]:
        print(node, end=" ")
        visited[node] = True

        for i in range(len(graph[node])):   # ✅ FIX
            if graph[node][i] == 1 and not visited[i]:
                queue.append(i)
