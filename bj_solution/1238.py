import heapq
import sys

input = sys.stdin.readline
n,m,x = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [1e9] * (m+1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for idx, c in graph[now]:
            cost = dist + c
            if cost < distance[idx]:
                distance[idx] = cost
                heapq.heappush(q, (cost,idx))
    return distance

result = 0
for i in range(1,n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x]+ back[i])

print(result)
