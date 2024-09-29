def solution():
    N, M = map(int, input().split())
    b = [0]*(N+1)
    for _ in range(M):
        i,j,k = map(int, input().split())
        for idx in range(i,j+1):
            b[idx]=k

    print(" ".join(str(num) for num in b[1:]))
solution()