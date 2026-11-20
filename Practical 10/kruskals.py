

def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex] 

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
    return True
def kruskal(vertices, edges):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    mst = []
    total_cost = 0  

    edges.sort(key=lambda edge: edge[2])

    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == len(vertices) - 1:
                break

    if len(mst) != len(vertices) - 1:
        print("Minimum spanning tree does not exist.")
        return

    print("\nEdges in Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, ":", weight)

    print("Total cost:", total_cost)


n = int(input("Enter number of vertices: "))
vertices = []

for i in range(n):
    vertex = input("Enter vertex name: ")
    vertices.append(vertex)

m = int(input("Enter number of edges: "))
edges = []

for i in range(m):
    print("Enter edge", i + 1, "(source destination weight):")
    u, v, weight = input().split()
    edges.append((u, v, int(weight)))

kruskal(vertices, edges)
