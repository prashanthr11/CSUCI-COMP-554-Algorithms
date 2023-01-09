MATCH = 0
MISMATCH = 1
GAP = 2


def dynamic_alignment(a, b):
    '''
    Time Complexity: O(N*M) where N amd M are lengths of the given strings
    Space Complexity: O(N*M)
    '''
    n, m = len(a), len(b)

    dp = [[0]*(m + 1) for i in range(n + 1)]

    for i in range(1, m + 1):
        dp[0][i] = i * GAP

    for j in range(1, n + 1):
        dp[j][0] = j * GAP

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            matched = MATCH if a[i - 1] == b[j - 1] else MISMATCH
            
            top = dp[i - 1][j] + GAP
            left = dp[i][j - 1] + GAP
            diagonal = dp[i - 1][j - 1] + matched
            dp[i][j] = min(top, left, diagonal)

    print(dp[-1][-1])

    for i in dp:
        print(*i)


def main():
    a = "occurrence"
    b = "ocurrance"

    a = "abc"
    b = "dea"

    dynamic_alignment(a, b)


if __name__ == "__main__":
    main()
