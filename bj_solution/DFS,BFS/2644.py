import sys

def dfs(node,cnt):
    visited[node] = True
    cnt += 1
    if node == b:
        res.append(cnt)
    for i in graph[node]:
        if not visited[i]:
            dfs(i,cnt)

input = sys.stdin.readline
n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    c,d = map(int,input().split())
    graph[c].append(d)
    graph[d].append(c)

res = []
visited = [False]*(n+1)
dfs(a,0)

if len(res) == 0:
    print(-1)
else:
    print(res[0]-1)

#######
import sys
from collections import deque


def bfs(node):
    q = deque([node])
    while q:
        n = q.popleft()
        for i in graph[n]:
            if visited[i] == 0:
                visited[i] = visited[n]+1
                q.append(i)


input = sys.stdin.readline
n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    c,d = map(int,input().split())
    graph[c].append(d)
    graph[d].append(c)

visited = [0]*(n+1)
bfs(a)

print(visited[b] if visited[b] > 0 else -1)