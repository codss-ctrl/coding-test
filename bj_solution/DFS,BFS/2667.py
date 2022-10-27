def in_range(x,y):
    return 0<=x<n and 0<=y<n


def dfs(x,y):
    global num
    if not in_range(x,y):
        return False
    if graph[x][y] == 1:
        global cnt
        graph[x][y] = num
        cnt += 1
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            dfs(nx,ny)
        return True
    return False

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
result = 0
cnt = 0
num = []
dxs,dys = [0,-1,0,1],[1,0,-1,0]
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)
for i in num:
    print(i)

###################

from collections import deque

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 0
    cnt = 1
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if in_range(nx,ny) and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
num = []
dxs,dys = [0,-1,0,1],[1,0,-1,0]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            num.append(bfs(i,j))

num.sort()
print(len(num))
for i in num:
    print(i)