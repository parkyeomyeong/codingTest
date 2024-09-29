def solution():
    A, B = map(int, input().split())
    answer = 0 
    per = []
    num = 0
    while B > len(per):
        num += 1
        per += [num]*num

    for i in range(A-1, B):
        answer += per[i]
    print(answer)

solution()