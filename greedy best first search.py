import heapq

def greedy(start, goal):
    pq = []
    heapq.heappush(pq, (h[start], start))
    visited = set()
    parent = {start: None}

    while pq:
        _, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                parent[nei] = node
                heapq.heappush(pq, (h[nei], nei))

# -------- INPUT --------
n = int(input("Enter number of edges: "))

graph = {}
print("Enter edges (u v):")
for _ in range(n):
    u, v = input().split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, [])

h = {}
print("Enter heuristic values:")
for _ in range(len(graph)):
    node, val = input().split()
    h[node] = int(val)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = greedy(start, goal)
print("Greedy Best First Path:", path)
