
def lcs(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = ""
    i = m
    j = n

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result = s1[i - 1] + result
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return result


s1 = input("Enter first sequence: ")
s2 = input("Enter second sequence: ")

ans = lcs(s1, s2)

print("Longest Common Subsequence:", ans)
print("Length:", len(ans))
