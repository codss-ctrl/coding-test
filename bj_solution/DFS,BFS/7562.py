from collections import deque


def in_range(x, y):
    return 0 <= x < L and 0 <= y < L


def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            print(graph[x2][y2]-1)
            return
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not graph[nx][ny]:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1


t = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
for _ in range(t):
    L = int(input())
    graph = [[0] * L for _ in range(L)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    bfs(x1, y1)