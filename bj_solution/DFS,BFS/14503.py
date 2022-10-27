import sys


n,m = map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx,dy = [-1,0,1,0],[0,1,0,-1]
visited = [[0]*m for _ in range(n)]
visited[r][c] = 1
cnt = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def turn_left(d):
    return (d+3)%4

while True:
    flag = False
    for _ in range(4):
        d = turn_left(d)
        nx,ny = r+dx[d],c+dy[d]
        if in_range(nx,ny) and graph[nx][ny] == 0 and not visited[nx][ny]:
            cnt += 1
            visited[nx][ny] = 1
            r,c = nx,ny
            flag = True
            break
    if not flag:
        if graph[r-dx[d]][c-dy[d]] == 1:
            print(cnt)
            break
        else:
            r,c = r-dx[d],c-dy[d]