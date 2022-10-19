import sys

input = sys.stdin.readline
cnt = 0
res = 0
for _ in range(4):
    out, ins = map(int, input().split())
    if cnt == 0:
        cnt += ins
    else:
        cnt -= out
        cnt += ins
    res = max(res, cnt)
print(res)