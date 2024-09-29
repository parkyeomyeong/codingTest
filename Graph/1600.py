from collections import deque

def solution():
    move = [(1,0), (0,1), (0,-1), (-1,0)]
    h_move = [(2,-1),(2,1),(1,-2),(1,2),(-1,-2),(-1,2),(-2,-1),(-2,1)]

    K = int(input())
    W, H = map(int, input().split())
    Map = []
    for _ in range(H):
        Map.append(list(map(int, input().split())))
    

    visited = [[[-1]*(K+1) for _ in range(W)] for _ in range(H)]
    answer = []

    q = deque([])
    q.append((0,0,0,0))

    while q:
        y,x,k_cnt,cnt = q.popleft()

        #if k_cnt == K: continue

        if y == H-1 and x == W-1:
            return cnt
    
        for ny, nx in move:
            ny, nx = ny+y, nx+x
            if 0 <= ny < H and 0 <= nx < W:
                if visited[ny][nx][k_cnt] == -1 and Map[ny][nx] == 0:
                    visited[ny][nx][k_cnt] = cnt + 1
                    q.append((ny,nx,k_cnt,cnt+1))

        if k_cnt < K:
            for ny, nx in h_move:
                ny, nx = ny+y, nx+x
                if 0 <= ny < H and 0 <= nx < W:
                    if visited[ny][nx][k_cnt+1] == -1 and Map[ny][nx] == 0:
                        visited[ny][nx][k_cnt+1] = cnt + 1
                        q.append((ny,nx,k_cnt+1,cnt+1))


    return -1

print(solution())