import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)

def solution():
    M, N = map(int, sys.stdin.readline().split())
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    dp = [[-1]*N for _ in range(M)]
    
    def dfs(y,x):
        if y == M-1 and x == N-1 :
            return 1

        if dp[y][x] == -1:
            dp[y][x] = 0
            for ny,nx in [(-1,0), (0,1), (0,-1) ,(1,0)]:
                ny,nx= ny+y,nx+x
                if 0<=ny<M  and 0<=nx<N:
                    if m[y][x] > m[ny][nx]:
                        dp[y][x] += dfs(ny,nx)
        return dp[y][x]
    
    print(dfs(0,0))

solution()