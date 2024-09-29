from collections import deque

def solution():
    N = int(input())
    m = []
    answer = 0
    for i in range(N):
        m.append(list(map(int, input().split())))
        for j in range(N):
            if m[i][j]==9:
                shark = [i,j,2,0] # 시작위치y, 시작위치x, 크기, 
                m[i][j] = 0
                break
    while True:
        time = bfs2(N, m, shark)
        if time == 0:
            break

        answer += time

    print(answer)

def bfs(N, m, shark):
    q = deque([])
    q.append([shark[0], shark[1],0])

    visited = [[False] * N for _ in range(N)]
    visited[shark[0]][shark[1]] = True

    mt = 1e9
    # 가장 가까운 물고기 목록 구하기
    while q:
        y,x,t= q.popleft()
        
        for ny, nx in [(1,0), (-1,0), (0,1), (0,-1)]:
            ny, nx = ny+y, nx+x
            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
            if visited[ny][nx] == True : continue

            if m[ny][nx] == 0: #no fish
                visited[ny][nx] = True
                q.append([ny, nx,t+1])
            elif m[ny][nx] == shark[2]:
                visited[ny][nx] = True
                q.append([ny, nx,t+1])
            elif m[ny][nx] < shark[2]:
                m[ny][nx] = 0 
                shark[0], shark[1] = ny,nx
                shark[3] += 1
                if shark[3] == shark[2]:
                    shark[2]+=1
                    shark[3]=0
                return t+1
            
    #위, 좌 순으로 정렬 후 해당 물고기 먹기


    return 0

def bfs2(N, m, shark):
    q = deque([])
    q.append([shark[0], shark[1], 0])

    visited = [[False] * N for _ in range(N)]
    # 먹을수 있는 가까운 물고기 목록
    fishes = []
    mt = 1e9
    while q:
        y,x,t = q.popleft()
        visited[y][x] = True

        #최소 거리 물고기가 나왔을떄 지금 탐색 시간이 많다면 조기 취소
        if t+1 > mt: continue

        for ny, nx in [(1,0), (-1,0), (0,-1), (0,1)]:
            ny, nx = ny+y, nx+x
            if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
            if visited[ny][nx] == True : continue
            if m[ny][nx] > shark[2]: continue

            if m[ny][nx] == 0 or m[ny][nx] == shark[2]:
                visited[ny][nx] = True
                q.append([ny,nx,t+1])
            else:
                visited[ny][nx] = True
                if len(fishes) == 0:
                    mt = t+1
                fishes.append([ny,nx,t+1])

    if len(fishes) > 0 :
        fishes.sort(key= lambda x:(x[0], x[1]))
        y,x,t = fishes[0]
        m[y][x] = 0

        shark[0], shark[1] = y,x
        shark[3] += 1
        if shark[3] == shark[2]:
            shark[2]+=1
            shark[3]=0

        return t
    
    return 0
                


solution()