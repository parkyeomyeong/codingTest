import sys
from collections import deque

def solution(): # 3264 ms
    t = int(sys.stdin.readline())

    for _ in range(t):
        # 데이터 입력 및 준비 Start
        n = int(sys.stdin.readline())
        visited = {}
        destinations = []    

        sx, sy = map(int, sys.stdin.readline().split())
        if visited.get(sx) == None: visited[sx] = {}
        visited[sx][sy] = False
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().split())
            if visited.get(x) == None: visited[x] = {}
            visited[x][y] = False

            destinations.append([x,y])

        dx, dy = map(int, sys.stdin.readline().split())

        if visited.get(dx) == None: visited[dx] = {}
        visited[dx][dy] = False
        destinations.append([dx, dy])

        # 데이터 입력 및 준비 End
        q = deque([])
        q.append([sx,sy,20])

        while q:
            x,y,b = q.popleft()
            visited[x][y] = True
            for nx, ny in destinations:
                dist = abs(x-nx) + abs(y-ny)
                ab_dist = b*50
                if dist > ab_dist: continue
                if visited[nx][ny] == True: continue
                
                q.append([nx,ny,20])

        print("happy" if visited[dx][dy] == True else "sad")
        
solution()