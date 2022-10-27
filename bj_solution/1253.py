import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0
for i in range(n):
    tmp = arr[:i] + arr[i+1:]
    left, right = 0, len(tmp)-1
    while left < right:
        t = tmp[left] + tmp[right]
        if t == arr[i]:
            cnt += 1
            break
        elif t < arr[i]:
            left += 1
        else:
            right -= 1
print(cnt)