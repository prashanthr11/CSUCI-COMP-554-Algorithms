x = "01101110"
y = "10101000"
z = "0110110011101000"


def shuffle_dp(x, y, z):
    '''
    Time Complexity: O(N*M) where N and M are lengths of x and y respectively
    Space Complexity: O(N*M)
    '''
    n = len(x)
    m = len(y)

    if len(z) != n + m:
        return "Impossible!"

    dp = [[0]*(m) for i in range(n)]

    dp[0][0] = 1
    for i in range(1, n):
        dp[i][0] = int(dp[i - 1][0] and x[i - 1] == z[i - 1])

    for j in range(1, m):
        dp[0][j] = int(dp[0][j - 1] and y[j - 1] == z[j - 1])

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = int(dp[i - 1][j] and (x[i - 1] == z[i + j - 1])
                           or (dp[i][j - 1] and (y[j - 1] == z[i + j - 1])))

    for i in dp:
        print(*i)

    return "yes" if dp[-1][-1] else "no"


if __name__ == "__main__":
    print(shuffle_dp(x, y, z))
