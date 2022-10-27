from collections import deque
import sys

n,m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i,j))

def in_range(x,y):
    return 0<= x<n and 0<=y<m

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    seaList = []
    while q:
        x,y = q.popleft()
        sea = 0
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if in_range(nx,ny):
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x,y,sea))
    for x,y,sea in seaList:
        graph[x][y] = max(0,graph[x][y] - sea)
    return 1

dxs,dys = [1,-1,0,0],[0,0,-1,1]
year = 0
while ice:
    visited = [[0]*m for _ in range(n)]
    melt = []
    cnt = 0
    for i,j in ice:
        if graph[i][j] and not visited[i][j]:
            cnt += bfs(i,j)
        if graph[i][j] == 0:
            melt.append((i,j))
    if cnt > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(melt)))
    year += 1

else:
    print(0)
