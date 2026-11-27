def prim(graph, start):
    selected = set()
    selected.add(start)

    mst = []
    total_cost = 0

    while len(selected) < len(graph):
        min_weight = float('inf')
        edge = None

        for u in selected:
            for v, weight in graph[u]:
                if v not in selected and weight < min_weight:
                    min_weight = weight
                    edge = (u, v, weight)

        if edge is None:
            print("Graph is not connected")
            return

        u, v, weight = edge
        mst.append(edge)
        total_cost += weight
        selected.add(v)

    print("\nMinimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, ":", weight)

    print("Total Minimum Cost:", total_cost)


graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex: ")
    graph[vertex] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v, w = input("Enter edge (u v weight): ").split()
    w = int(w)

    graph[u].append((v, w))
    graph[v].append((u, w))

start = input("Enter starting vertex: ")

prim(graph, start)