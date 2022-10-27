import sys
from collections import deque

def bfs(graph,start,visited):
    q = deque([start])
    visited[start] = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    print(sum(visited[2:]))

input = sys.stdin.readline
n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for _ in range(n+1)]
bfs(graph,1,visited)
