def union(parents, node1, node2):
    node1, node2 = find(parents, node1), find(parents, node2)
    parents[node2] = node1

def find(parents, node):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
        return parents[node]
    return node
    
def solution():
    N = int(input())
    M = int(input())
    lines = []
    parents = [i for i in range(N+1)]
    answer, edge_cnt = 0, 0 
    for _ in range(M):
        lines.append(list(map(int, input().split())))

    lines.sort(key= lambda x:x[2])

    for c1, c2, cost in lines:
        if find(parents, c1) != find(parents, c2):
            union(parents, c1, c2)
            answer += cost
            edge_cnt += 1

        if edge_cnt == N-1:
            break

    print(answer)

solution()