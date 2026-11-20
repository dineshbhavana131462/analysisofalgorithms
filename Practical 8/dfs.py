
def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


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

visited = set()

print("DFS Traversal:")
dfs(graph, start, visited)
