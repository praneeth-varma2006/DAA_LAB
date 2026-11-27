
def tsp(graph, n):
    INF = float('inf')

    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if not (mask & (1 << v)):
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(
                            dp[new_mask][v],
                            dp[mask][u] + graph[u][v]
                        )

    full_mask = (1 << n) - 1
    ans = INF

    for i in range(1, n):
        ans = min(ans, dp[full_mask][i] + graph[i][0])

    print("Minimum travelling cost:", ans)


n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

tsp(graph, n)
