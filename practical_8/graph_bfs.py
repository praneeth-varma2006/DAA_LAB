from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    graph[vertex] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = input("Enter edge (u v): ").split()

    graph[u].append(v)
    graph[v].append(u)

start = input("Enter starting vertex: ")

print("BFS Traversal:")
bfs(graph, start)