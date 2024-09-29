from collections import deque

def solution():
    answer = 0
    N = int(input())
    m = [[0]*(N+1) for _ in range(N+1)]
    #사과 
    K = int(input())
    for _ in range(K):
        y, x = map(int, input().split())
        m[y][x] = 2
    #변환정보
    L = int(input())
    cmd = ['N']*10001
    for _ in range(L):
        X, C = map(str, input().split())
        cmd[int(X)] = C

    snk = deque(())
    snk.append((1,1))
    m[1][1] = 1

    move = (0,1)

    while True:
        
        #방향 전환 여부
        if cmd[answer] != 'N':
            vy, vx = move
            # x 축 방향
            if vx != 0:
                if cmd[answer] == 'L':
                    move = [-vx, vy]
                if cmd[answer] == 'D':
                    move = [vx, vy]
            # y 축 방향
            else:
                if cmd[answer] == 'L':
                    move = [vx, vy]
                if cmd[answer] == 'D':
                    move = [vx, -vy]

        ny, nx = snk[-1][0] + move[0], snk[-1][1] + move[1]

        if 1 > ny or ny > N or 1 > nx or nx > N or m[ny][nx] == 1:
            break
        # if 1 > ny or 1 > nx : 
        #     answer += 1
        #     break

        # if ny > N or nx > N or m[ny][nx] == 1: break
    

        #다음이 사과가 아니면 꼬리 제거
        if m[ny][nx] != 2:
            ty, tx = snk.popleft()
            m[ty][tx] = 0

        snk.append((ny,nx))
        m[ny][nx] = 1

        answer += 1

    return answer + 1

print(solution())
