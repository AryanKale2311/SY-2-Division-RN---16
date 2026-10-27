"""
Longest Common Subsequence (LCS) using Dynamic Programming (Bottom-Up / Tabulation)
--------------------------------------------------------------------------------
Formula reminder:
    If characters match:      dp[i][j] = dp[i-1][j-1] + 1
    If characters don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""


def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Step 1: Create DP table of size (m+1) x (n+1), filled with 0
    # The extra row/column represent the empty string (base case)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the table using the bottom-up approach
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                # Characters match -> take diagonal value + 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Characters differ -> take the max of top or left
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: The length of the LCS is in the bottom-right cell
    length = dp[m][n]

    # Step 4: Backtrack through the table to reconstruct the actual subsequence
    subsequence = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            subsequence.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subsequence.reverse()
    lcs_string = "".join(subsequence)

    return length, lcs_string, dp


def print_dp_table(X, Y, dp):
    """Nicely prints the DP table with row/column labels."""
    header = ["", ""] + list(Y)
    print("\t".join(header))

    for i in range(len(dp)):
        row_label = "" if i == 0 else X[i - 1]
        row = [row_label] + [str(val) for val in dp[i]]
        print("\t".join(row))


if __name__ == "__main__":
    # Input
    X = input("Enter first sequence: ")
    Y = input("Enter second sequence: ")

    # Output
    length, subsequence, dp = lcs(X, Y)

    print("\nDP Table:")
    print_dp_table(X, Y, dp)

    print(f"\nLength of LCS: {length}")
    print(f"LCS String: {subsequence}")