
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter the amount: "))

dp = [float('inf')] * (amount + 1)

dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], 1 + dp[i - coin])

if dp[amount] == float('inf'):
    print("Change cannot be made")
else:
    print("Minimum coins required:", dp[amount])
