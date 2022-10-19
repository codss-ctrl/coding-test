import sys

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split(" "))
    y = N % H
    x = N // H + 1
    if N % H == 0:
        y = H
        x = N // H
    print(str(y) + str(x).zfill(2))
