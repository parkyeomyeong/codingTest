def solution():
    N,M = map(int, input().split())
    boxs = [i for i in range(N+1)]
    r = []
    for _ in range(M):
        r.append(list(map(int, input().split())))

    for i, j in r:
        for v in range((j-i+1)//2):
            temp = boxs[i+v]
            boxs[i+v] = boxs[j-v]
            boxs[j-v] = temp
        
    boxs.pop(0)
    print(" ".join(str(box) for box in boxs))
    return

solution()