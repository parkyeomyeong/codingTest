def solution():
    N = int(input())
    lines = []
    dp = [1]*N
    for _ in range(N):
        lines.append(list(map(int, input().split())))

    lines.sort()
    
    for front in range(1,N):
        for back in range(0,front):
            #현 왼쪽과 연결된 오른쪽선이 이전선과 겹치지 않을떄 max 개수 업데이트
            if lines[front][1] > lines[back][1]:
                dp[front] = max(dp[front], dp[back] + 1)

    # 현 줄이 이전꺼보다 앞에있으면 +1 
    print(N-max(dp))

solution()