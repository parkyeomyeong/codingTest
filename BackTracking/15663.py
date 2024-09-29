def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    dic = {}

    #처음부터 문자열로 받지 않은 이유는 문자열과 숫자의 정렬은 다르기 때문
    nums.sort()
    nums = [str(num) for num in nums]
    visited = [False for _ in range(N+1)]

    for i in range(N):
        visited[i] = True
        answer = [nums[i]]
        func(nums, visited, dic, N, M, answer)
        visited[i] = False

def func(nums, visited, dic, n, r, answer):
    if len(answer) == r:
        if not dic.get(" ".join(answer)):
            dic[" ".join(answer)] = True
            print(" ".join(answer))
        return
    
    for i in range(n):
        if visited[i] == False:
            cur_answer = answer + [nums[i]]

            visited[i] = True
            func(nums, visited, dic, n, r, cur_answer)
            visited[i] = False


solution()