def solution():
    answer = [0, '0', '0']

    for y in range(9):
        rows = list(map(int, input().split()))
        for x in range(9):
            if answer[0] <= rows[x]:
                answer = [rows[x], str(y+1), str(x+1)]

    print(answer[0])
    print(" ".join(answer[1:]))

solution()
