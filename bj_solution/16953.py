import sys
input = sys.stdin.readline

a,b = map(int, input().split())
cnt = 1
while True:
    if a == b:
        print(cnt)
        break
    elif a > b:
        print(-1)
        break
    elif b % 10 == 1:
        b //= 10
        cnt += 1
    elif b % 2 == 0:
        b //= 2
        cnt += 1
    else:
        print(-1)
        break

## 양방향 큐
import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int, input().split())
q = deque()
q.append((a,1))
while q:
    n, cnt = q.popleft()
    if n > b:
        continue
    if n == b:
        print(cnt)
        break
    q.append((int(str(n)+'1'), cnt +1))
    q.append((n*2, cnt +1))
else:
    print(-1)