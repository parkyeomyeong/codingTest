import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

def dfs(h,w,y,x,m,visited,answer):
    if y == h-1 and x == w-1 :
        answer[0] += 1
        return
    
    for ny,nx in [(-1,0), (0,1), (0,-1) ,(1,0)]:
        ny,nx= ny+y,nx+x
        if 0<=ny<h and 0<=nx<w:
            if visited[ny][nx] == False and m[y][x] > m[ny][nx]:
                visited[ny][nx] = True
                dfs(h,w,ny,nx,m,visited,answer)
                visited[ny][nx] = False

def solution():
    M, N = map(int, sys.stdin.readline().split())
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    answer = [0]

    visited[0][0] = True
    dfs(M,N,0,0,m,visited,answer)

    print(answer[0])

solution()