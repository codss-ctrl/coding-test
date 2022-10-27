import sys
import heapq

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def dijkstra(x,y):
    q = []
    dist = [[1e9] * n for _ in range(n)]
    heapq.heappush(q, (x,y))
    dist[x][y] = graph[x][y]

    while q:
        cur_x, cur_y = heapq.heappop(q)
        cur_cost = dist[cur_x][cur_y]
        for dx,dy in zip(dxs,dys):
            nx = cur_x + dx
            ny = cur_y + dy
            if in_range(nx,ny):
                cost = cur_cost + graph[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heapq.heappush(q,(nx,ny))
    return dist[n-1][n-1]

input = sys.stdin.readline
round = 1
dxs,dys = [-1,0,1,0],[0,1,0,-1]

while True:
    n = int(input())
    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    result = dijkstra(0,0)
    print(f'Problem {round}: {result}')
    round += 1



