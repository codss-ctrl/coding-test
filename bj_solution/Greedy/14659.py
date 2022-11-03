n = int(input())
arr = list(map(int, input().split()))
MAX = 0
cnt = 0
res = 0
for i in arr:
    if i > MAX:
        MAX = i
        cnt = 0
    else:
        cnt += 1
    res = max(cnt, res)
print(res)
