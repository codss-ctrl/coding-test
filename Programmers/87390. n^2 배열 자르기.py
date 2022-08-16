import math


def solution(n, left, right):
    grid = []
    for i in range(left, right+1):
        j = math.floor(i/n) - i%n
        if j < 0 :
            j = 0
        else:
            j = j
        grid.append((i % n + 1 + j))
    return grid
n,l,r = 3,2,5
# n,l,r = 4,7,14

print(solution(n,l,r))