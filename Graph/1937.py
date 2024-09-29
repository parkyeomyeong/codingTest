from collections import deque
import heapq
import sys


def bfs1(n,m,y,x):
    #방문 맵 그리기
    visited =  []
    visited.append([True]*(n+2))
    for _ in range(n):
        visited.append([True]+[False]*n+[True])
    visited.append([True]*(n+2))

    q = deque([])
    q.append((y,x,1))
    visited[y+1][x+1] = True

    max_cnt = 0
    while q:
        cy,cx,cnt = q.popleft()
        max_cnt = max(max_cnt, cnt)

        for ny,nx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny += cy
            nx += cx
            if visited[ny][nx] == False:
                if m[cy-1][cx-1] < m[ny-1][nx-1]:
                    visited[ny][nx] = True
                    q.append((ny,nx,cnt+1))
    return max_cnt

def bfs2(n, m, cnt_m, y, x):
    
    q = deque([])
    q.append((y,x))

    max_cnt = 1
    while q:
        cy,cx = q.popleft()
        max_cnt = max(max_cnt, cnt_m[cy][cx])

        for ny,nx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny += cy
            nx += cx
            if 0 <= ny < n and 0 <= nx < n:
                if m[cy][cx] > m[ny][nx]: # 다음 대나무 양이 지금보다 큰 경우
                    if cnt_m[cy][cx] >= cnt_m[ny][nx]:
                        cnt_m[ny][nx] = cnt_m[cy][cx] + 1
                        q.append((ny,nx))
    
    return max_cnt

def solution():
    n = int(input())
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    answer = 0 
    for i in range(n):
        for j in range(n):
            answer = max(bfs1(n,m,i,j), answer)

    print(answer)

def solution2():
    n = int(input())
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    #방문 맵 그리기
    cnt_m = [[0]*n for _ in range(n)]

    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(bfs2(n,m,cnt_m,i,j), answer)

    print(answer)

import sys
sys.setrecursionlimit(10**9)
def function(m, dp, n, y, x):
    if dp[y][x] != 0:
        return dp[y][x]

    # 처음 도착하면 우선 1
    dp[y][x] = 1
    for ny,nx in [(-1,0), (1,0), (0,-1), (0,1)]:
        ny, nx = ny+y, nx+x
        if 0<=ny<n and 0<=nx<n:
            if m[y][x] < m[ny][nx]:
                dp[y][x] = max(dp[y][x], function(m,dp,n,ny,nx) + 1)

    return dp[y][x]
def solution3():
    answer = 1
    n = int(sys.stdin.readline())
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                answer = max(answer, function(m,dp,n,i,j))
        
    print(answer)

solution()


solution3()