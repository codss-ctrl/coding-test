from collections import deque

def in_range(x,y):
    return 0<=x<n and 0<=y<m

dx,dy=[0,1,0,-1],[1,0,-1,0]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = True

T = int(input())
for _ in range(T):
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    print(cnt)