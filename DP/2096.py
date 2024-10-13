import sys

def solution():
    N = int(sys.stdin.readline())

    dpmax = [0,0,0]
    dpmin = [0,0,0]

    for _ in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        line_copy = line[:]
        line_copy[0] += max(dpmax[0], dpmax[1])
        line_copy[1] += max(dpmax)
        line_copy[2] += max(dpmax[1], dpmax[2])
        dpmax = line_copy
        line_copy = line[:]
        line_copy[0] += min(dpmin[0], dpmin[1])
        line_copy[1] += min(dpmin)
        line_copy[2] += min(dpmin[1], dpmin[2])
        dpmin = line_copy

    print(max(dpmax), min(dpmin))

solution()
