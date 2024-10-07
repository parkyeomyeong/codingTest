import sys
import heapq

def dik(graph, distancese, node):
    pq = []
    heapq.heappush(pq, (0, node))
    distancese[node] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        # 지금까지거리가 현거리보다 크면 이미 방문한거임
        if dist > distancese[now] : continue

        for n_node, n_dist in graph[now]:
            #지금까지 거리 합이 현 거리보다 작으면 방문 및 업데이트
            if n_dist + dist < distancese[n_node]:
                distancese[n_node] = n_dist + dist
                heapq.heappush(pq, (n_dist + dist, n_node))

def solution():
    N,D = map(int, sys.stdin.readline().split())

    graph = [[[i+1,1]] for i in range(20000)]
    graph.append([]) #마지막에 아무것도 안들어가서 임의 추가
    distancese = [1e9]*20001
    for _ in range(N):
        s,e,r = map(int, sys.stdin.readline().split())
        graph[s].append([e,r])
    
    dik(graph, distancese, 0)

    print(distancese[D])
solution()
