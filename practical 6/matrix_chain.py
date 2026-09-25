def matrix_chain(p):
    n = len(p) - 1

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]

                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]


n = int(input("Enter number of matrices: "))

p = list(map(int, input("Enter dimensions: ").split()))

print("Minimum multiplication =", matrix_chain(p))
