from collections import deque

def bfs(n, m, start_y, start_x, mapp):
    q = deque([])
    q.append([start_y, start_x, 0])
    visited = [[False] * m for _ in range(n)]

    while q:
        ly, lx, d = q.popleft()
        if mapp[ly][lx] == 2: return d

        for ny, nx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = ny + ly, nx + lx
            if 0 <= ny < n and 0 <= nx < m:
                if mapp[ny][nx] != 0 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append([ny,nx,d+1])

def solution():
    n,m = map(int, input().split())
    mapp = []
    answer = [[0]*m for _ in range(n)]

    for _ in range(n):
        mapp.append(list(map(int, input().split())))

    for y in range(n):
        for x in range(m):
            if mapp[y][x] == 1:
                answer[y][x] = bfs(n,m,y,x,mapp)

    for y in range(n):
        print(" ".join(str(i) for i in answer[y]))

from collections import deque

def solution2():
    n,m = map(int, input().split())
    mapp = []
    answer = [[-1]*m for _ in range(n)]
    start = []
    for y in range(n):
        arr = list(map(int, input().split()))
        mapp.append(arr)
        for x in range(m):
            if arr[x] == 2:
                start = [y,x]

    q = deque([])
    q.append([start[0], start[1], 0])
    while q:
        ly, lx, d = q.popleft()
        for ny, nx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = ny + ly, nx + lx
            if 0 <= ny < n and 0 <= nx < m:
                if mapp[ny][nx] == 1 and answer[ny][nx] == -1:
                    answer[ny][nx] = d+1
                    q.append([ny,nx,d+1])

    #벽은 0으로 고치기
    for y in range(n):
        for x in range(m):
            if answer[y][x] == -1:
                if mapp[y][x] ==2 or mapp[y][x] == 0:
                    answer[y][x] = 0
    for y in range(n):
        print(" ".join(str(i) for i in answer[y]))

solution2()