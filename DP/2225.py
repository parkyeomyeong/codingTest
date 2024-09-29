N, K = map(int, input().split())

dp = [[1]*(N+1) for _ in range(K)]

if K == 1:
    print(1)
else :
    for k in range(1,K):
        for n in range(1, N+1):
            dp[k][n] = dp[k][n-1] + dp[k-1][n]

    print(dp[k][n] % 1000000000)