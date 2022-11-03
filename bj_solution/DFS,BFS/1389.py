import sys
from collections import deque

def bfs(i):
    q = deque([i])
    num = [0]*(n+1)
    visited[i] = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                num[i] = num[node]+1
                visited[i] = 1
                q.append(i)
    return sum(num)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
result = []
for i in range(1,n+1):
    visited = [0] * (n + 1)
    result.append(bfs(i))
print(result.index(min(result))+1)