
n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix:")
print("Enter 999 for no direct connection")

dist = []

for i in range(n):
    row = list(map(int, input().split()))
    dist.append(row)

# Floyd-Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])

print("\nShortest distance matrix:")

for i in range(n):
    for j in range(n):
        if dist[i][j] >= 999:
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
