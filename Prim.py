
n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix (0 for no edge):")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

selected = [False] * n
selected[0] = True

edges = 0
total_cost = 0

print("\nMinimum Spanning Tree:")

while edges < n - 1:

    minimum = float('inf')
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    if minimum == float('inf'):
        print("Graph is disconnected!")
        break

    print(x + 1, "-", y + 1, ":", minimum)

    selected[y] = True
    total_cost += minimum
    edges += 1

print("Total Minimum Cost:", total_cost)
