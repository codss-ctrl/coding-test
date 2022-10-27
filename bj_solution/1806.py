import sys

input = sys.stdin.readline
n,s = map(int, input().split())
arr = list(map(int, input().split()))
l, r, tsum = 0, 0, 0
result = n+1

if sum == s:
    print(0)
    exit(0)

while True:
    if s <= tsum:
        result = min(r-l, result)
        tsum -= arr[l]
        l += 1
    elif r == n:
        break
    else:
        tsum += arr[r]
        r += 1

print(result) if result != n+1 else print(0)