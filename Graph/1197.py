def find_p(g, n):
    if g[n] != n:
        g[n] = find_p(g, g[n])
        return g[n]
    return n

def union_p(g,a,b):
    a_p, b_p = find_p(g, a), find_p(g, b)
    
    if a_p < b_p:
        g[b_p] = a_p
    elif a_p > b_p:
        g[a_p] = b_p

def solution():
    V, E = map(int, input().split())
    graph = [i for i in range(V+1)]
    edges = []
    answer = 0
    e_cnt = 0
    for _ in range(E):
        edges.append(list(map(int, input().split())))

    # 간선기준으로 오름차순 정렬
    edges.sort(key = lambda x:x[2])

    for node1,node2,value in edges:
        if find_p(graph, node1) != find_p(graph, node2):
            union_p(graph, node1, node2)
            answer += value
            e_cnt += 1

            if e_cnt == V-1:
                break

    print(answer)


solution()