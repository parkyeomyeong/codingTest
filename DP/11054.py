def solution():
    N = int(input())
    arr = list(map(int, input().split()))

    dp1 = [1]*N
    dp2 = [1]*N

    #왼쪽부터 증가 하는 최대 길이 dp로 구하기
    for i in range(1, N):
        for j in range(i):
            # 현재 기준이 이전꺼보다 크면 이전꺼길이 + 1, 현재 최대길이 중 큰거 넣기
            if arr[i] > arr[j]:
                dp1[i] = max(dp1[i], dp1[j]+1)

    #오른쪽부터 감소하는 최대 길이 dp로 구하기
    for i in range(N-1,-1,-1):
        for j in range(N-1,i,-1):
            # 현재 기준이 이전꺼보다 크면 이전꺼길이 + 1, 현재 최대길이 중 큰거 넣기
            if arr[i] > arr[j]:
                dp2[i] = max(dp2[i], dp2[j]+1)
    
    answer = 1
    for i in range(N):
        answer = max(answer, dp1[i]+dp2[i])
    print(answer-1)
        

solution()