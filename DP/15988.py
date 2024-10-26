import sys
def solution():
    T = int(sys.stdin.readline())
    tc = [int(sys.stdin.readline()) for _ in range(T)]
    mtc = max(tc)
    dp = [0]*(mtc+1)

    # 1-> 1, 2=> 2, 3=>3, 4=>7
    dp[1],dp[2],dp[3],dp[4]=1,2,4,7

    for i in range(5,mtc+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%1000000009

    for c in tc:
        print(dp[c])

solution()

# def solution2():
#     T = int(sys.stdin.readline())
#     for _ in range(T):
#         n = int(sys.stdin.readline())
#         dp = [0]*(n+1)
#         # 1-> 1, 2=> 2, 3=>3, 4=>7
#         dp[1],dp[2],dp[3],dp[4]=1,2,4,7
#         for i in range(5,n+1):
#             dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

#         print(dp[n]%1000000009)

# solution2()