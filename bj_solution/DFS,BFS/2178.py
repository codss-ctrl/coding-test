import sys
from collections import deque


def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs(x,y):
    global cnt
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx, y+dy
            if in_range(nx,ny) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

    return graph[n-1][m-1]

input = sys.stdin.readline
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
dxs,dys = [-1,0,1,0],[0,1,0,-1]
cnt = bfs(0,0)
print(cnt)