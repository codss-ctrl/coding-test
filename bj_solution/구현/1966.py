from collections import deque

T = int(input())
for _ in range(T):
    n,m = map(int, input().split(' '))
    pr = deque(map(int, input().split(' ')))
    mark = deque([0 for _ in range(n)])
    mark[m] = 1
    cnt = 0
    while True:
        if pr[0] == max(pr):
            cnt += 1
            if mark[0] == 1:
                print(cnt)
                break
            else:
                pr.popleft()
                mark.popleft()
        else:
            p = pr.popleft()
            pr.append(p)
            m = mark.popleft()
            mark.append(m)
