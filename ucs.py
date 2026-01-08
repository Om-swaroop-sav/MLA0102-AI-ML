import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('C', 2)],
    'C': [('E', 5)],
    'D': [('F', 2), ('G', 4)],
    'E': [('G', 3)],
    'F': [('G', 1)],
    'G': []
}

def ucs(start, goal):
    pq = [(0, start, [start])]   # (cost, node, path)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)
            for neigh, w in graph[node]:
                heapq.heappush(pq, (cost + w, neigh, path + [neigh]))

    return None

path, cost = ucs('A', 'G')
print("Path:", " -> ".join(path))
print("Cost:", cost)
