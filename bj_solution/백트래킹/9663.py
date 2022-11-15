n = int(input())
def n_queen(queen, x):
    cnt = 0
    n = len(queen)
    if x == n:
        return 1
    for i in range(n):
        queen[x] = i
        if promising(queen,x):
            cnt += n_queen(queen,x+1)
    return cnt

def promising(queen,x):
    for i in range(x):
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x-i):
            return False
    return True

print(n_queen([0]*n,0))