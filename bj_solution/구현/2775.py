T = int(input())
for _ in range(T):
    floor = int(input())
    n = int(input())
    if floor == 0:
        print(n)
        exit(0)
    elif n == 1:
        print(1)
        exit(0)
    zero = [i for i in range(1, n+1)]
    for k in range(floor):
        for i in range(1, n):
            zero[i] += zero[i-1]
print(zero[-1])