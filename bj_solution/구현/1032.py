import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))
res = arr[0]
for i in range(1,n):
    for j in range(len(arr[0])):
        if arr[i][j] != res[j]:
            res[j] = '?'
print(''.join(res))