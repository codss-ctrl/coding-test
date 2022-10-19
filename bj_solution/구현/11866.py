from collections import deque
n, k = map(int, input().split(' '))
q = deque([i for i in range(1,n+1)])
stack = []
print('<', end='')
while q:
    for _ in range(k-1):
        tmp = q.popleft()
        q.append(tmp)
    print(q.popleft(), end='')
    if q:
        print(', ', end='')
print('>', end='')
