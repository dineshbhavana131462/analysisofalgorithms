
from collections import deque

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("BFS Traversal:")

    while queue:

        vertex = queue.popleft()
        print(vertex, end=" ")

      
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input("Enter vertex name: ")
    neighbors = input(
        f"Enter neighbors of {vertex} separated by spaces: "
    ).split()

    graph[vertex] = neighbors

start = input("Enter starting vertex: ")
if start in graph:
    bfs(graph, start)
else:
    print("Starting vertex not found!")
