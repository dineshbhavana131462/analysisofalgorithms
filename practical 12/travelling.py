
from itertools import permutations

n = int(input("Enter number of cities: "))

graph = []

print("Enter the cost matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

cities = list(range(1, n))

min_cost = float('inf')
best_path = []

for path in permutations(cities):
    current_path = [0] + list(path) + [0]

    cost = 0

    for i in range(len(current_path) - 1):
        cost += graph[current_path[i]][current_path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = current_path

print("\nMinimum cost:", min_cost)

print("Shortest path:")
for city in best_path:
    print(city + 1, end=" ")
