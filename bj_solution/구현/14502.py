import copy
import sys
from collections import deque


def in_range(x,y):
    return 0<=x<n and 0<=y<m

def bfs():
    c_map = copy.deepcopy(maps)
    q = deque()
    for i in range(n):
        for j in range(m):
            if c_map[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny):
                if c_map[nx][ny] == 0:
                    c_map[nx][ny] = 2
                    q.append((nx,ny))
    global result
    cnt = 0
    for i in range(n):
        for j in range(m):
            if c_map[i][j] == 0:
                cnt += 1
    result = max(result, cnt)

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                make_wall(cnt+1)
                maps[i][j] = 0

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dxs, dys = [-1,0,1,0],[0,1,0,-1]
result = 0
make_wall(0)
print(result)