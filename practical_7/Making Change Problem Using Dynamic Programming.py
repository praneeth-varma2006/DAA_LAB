def making_change(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != float('inf') else -1


coins = list(map(int, input("Enter coin denominations: ").split()))

amount = int(input("Enter amount: "))

result = making_change(coins, amount)

if result != -1:
    print("Minimum number of coins required:", result)
else:
    print("Change is not possible")