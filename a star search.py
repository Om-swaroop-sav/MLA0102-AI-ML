import heapq

def astar(start, goal):
    pq = []
    heapq.heappush(pq, (h[start], 0, start))
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for nei, w in graph[node]:
            new_cost = g + w
            if nei not in cost or new_cost < cost[nei]:
                cost[nei] = new_cost
                parent[nei] = node
                heapq.heappush(pq, (new_cost + h[nei], new_cost, nei))

# -------- INPUT --------
n = int(input("Enter number of nodes: "))

graph = {}
print("Enter edges (node neighbour cost):")
for _ in range(n):
    u, v, w = map(str, input().split())
    w = int(w)
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, [])

h = {}
print("Enter heuristic values:")
for _ in range(len(graph)):
    node, val = input().split()
    h[node] = int(val)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = astar(start, goal)
print("A* Path:", path)
