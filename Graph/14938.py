import sys

def solution():
    n,m,r = sys.stdin.readline().split()
    itmes = list(map(int, sys.stdin.readline().split()))
    routes = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(r):
        a,b,l = map(int, sys.stdin.readline().split())
        routes[a][b] = l
        routes[b][a] = l

    #다익스트라 알고리즘 시작
    #방문
    #최대값저장
solution()