from collections import deque
import sys


def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    q = deque([v])
    visited[v] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in sorted(graph[node]):
            if not visited[i]:
                q.append(i)
                visited[i] = True

input = sys.stdin.readline
n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
dfs(graph,v,visited)
print()
visited = [False] * (n+1)
bfs(graph,v,visited)

