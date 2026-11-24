
def knapsack_top(wt, val, W, n, dp):
    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]

    if wt[n - 1] <= W:
        include = val[n - 1] + knapsack_top(wt, val, W - wt[n - 1], n - 1, dp)
        exclude = knapsack_top(wt, val, W, n - 1, dp)
        dp[n][W] = max(include, exclude)
    else:
        dp[n][W] = knapsack_top(wt, val, W, n - 1, dp)

    return dp[n][W]


def knapsack_bottom(wt, val, W, n):
    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
W = 5
n = len(wt)

dp = [[-1 for j in range(W + 1)] for i in range(n + 1)]

print("Top-Down:", knapsack_top(wt, val, W, n, dp))
print("Bottom-Up:", knapsack_bottom(wt, val, W, n))
