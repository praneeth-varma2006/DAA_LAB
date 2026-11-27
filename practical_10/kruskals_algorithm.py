
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal(vertices, edges):
    parent = {}
    rank = {}

    for v in vertices:
        parent[v] = v
        rank[v] = 0

    edges.sort(key=lambda x: x[2])

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            union(parent, rank, root_u, root_v)

    if len(mst) != len(vertices) - 1:
        print("Graph is not connected")
        return

    print("\nMinimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, ":", weight)

    print("Total Minimum Cost:", total_cost)


vertices = input("Enter vertices: ").split()

n = int(input("Enter number of edges: "))

edges = []

for i in range(n):
    u, v, w = input("Enter edge (u v weight): ").split()
    edges.append((u, v, int(w)))

kruskal(vertices, edges)
