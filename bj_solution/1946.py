import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x:x[0])
    cnt = 1
    cur = arr[0][1]
    for i in range(1,N):
        if arr[i][1] < cur:
            cur = arr[i][1]
            cnt += 1
    print(cnt)