from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)
visited[S] = 1
q = deque([S])
while q:
    now = q.popleft()
    for i in (now + U, now - D):
        if 0 < i <= F and not visited[i]:
            visited[i] = visited[now] + 1
            q.append(i)
print(visited[G]-1 if visited[G] > 0 else "use the stairs")
