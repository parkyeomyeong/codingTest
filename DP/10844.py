def solution():
    N = int(input())

    dp = [[1]*10 for _ in range(N)]
    dp[0][0] = 0

    #맨 앞에 자리수는 1~9
    #그 뒤에 자리수에 오는 숫자는 0~9
    
    # 두번쨰 자리수부터 돌면서 바로 앞자리 숫자와 계단수인경우 그 가짓수를 더하기
    for i in range(1,N):
        # 0과 9는 각각 1, 8 의경우만 계단수에 해당하므로 따로 계산
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1,9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    print(sum(dp[N-1])%1000000000)
            

solution()