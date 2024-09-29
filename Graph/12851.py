from collections import deque
def solution():
    N, K = map(int, input().split())
    l = [0]*100001
    cnt = [0]*100001

    if N == K : return 0, 1

    q = deque([])
    q.append((1, N))
    l[N] = 1
    cnt[N] = 1

    while q:
        t, cn = q.popleft()
        for nn in (cn-1, cn+1, cn*2):
            if 0 <= nn < 100001:
                if l[nn] == 0:
                    l[nn] = t
                    cnt[nn] += cnt[cn] 
                    q.append((t+1, nn))
                else :
                    if l[nn] == t:
                        cnt[nn] += cnt[cn] 
    return l[K], cnt[K]

for answer in solution():
    print(answer)

