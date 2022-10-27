import sys
from collections import deque


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(i,j,rain):
    q = deque([(i,j)])
    visited[i][j] = True
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if in_range(nx,ny) and graph[nx][ny] > rain and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))

n = int(input())
graph = []
MAX = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)
    MAX = max(MAX, max(tmp))

dxs,dys = [1,-1,0,0],[0,0,1,-1]

res = 0
for rain in range(MAX):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and not visited[i][j]:
                bfs(i,j,rain)
                cnt += 1
    res = max(res,cnt)

print(res)


#############

import sys
sys.setrecursionlimit(100000)

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dfs(x,y,rain):
    visited[i][j] = 1
    for dx,dy in zip(dxs,dys):
        nx,ny=x+dx,y+dy
        if in_range(nx,ny) and graph[nx][ny] > rain and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx,ny,rain)

n = int(input())
graph = []
MAX = 0
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)
    MAX = max(MAX, max(tmp))

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

res = 0
for rain in range(MAX):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > rain and not visited[i][j]:
                dfs(i,j,rain)
                visited[i][j] = 1
                cnt +=1
    res = max(res,cnt)
print(res)