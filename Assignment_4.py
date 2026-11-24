
def memoization(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = memoization(n - 1, dp) + memoization(n - 2, dp)
    return dp[n]


def tabulation(n):
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input("Enter n: "))

dp = [-1] * (n + 1)

print("Memoization:", memoization(n, dp))
print("Tabulation:", tabulation(n))
