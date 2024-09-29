from collections import deque

def bfs(m,N,M):
    q = deque([])
    visited = [[False]*M for _ in range(N)]

    q.append([0,0])
    melting_cnt = 0 
    while q:
        cy,cx = q.popleft()
        for ny, nx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny += cy
            nx += cx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False:
                if m[ny][nx] == 0:
                    q.append([ny,nx])
                elif m[ny][nx] == 1:
                    m[ny][nx] = 0
                    melting_cnt += 1
                visited[ny][nx] = True

    return melting_cnt


    
def solution():
    N,M = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    
    total_count, cur_count, prev_count = 0, 0, 0
    answer1, answer2 = 0, 0
    for y in range(N):
        for x in range(M):
            if m[y][x] == 1:
                total_count += 1

    while total_count:
        prev_count = total_count

        total_count -= bfs(m,N,M)
        answer1 += 1
        answer2 = prev_count

    print(answer1)
    print(answer2)

solution()