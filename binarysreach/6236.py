import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    nums = []
    
    max_burget = 0
    nums = [int(sys.stdin.readline()) for _ in range(N)]

    mi, ma = min(nums), sum(nums)
    
    while mi <= ma:
        m = (mi + ma)//2

        for num in nums:
            if m - num <= 0:
                m -= num
            else:
                



    print(mi)

    
solution()
