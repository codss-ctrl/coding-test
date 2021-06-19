import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호 입력받기
start_node = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start_node):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정
    heapq.heappush(q, (0, start_node))
    distance[start_node] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, cur_node = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[cur_node] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[cur_node]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start_node)

for i in range(1, n + 1):
    if distance[i] == INF:
        print(-1)
    else:
        print(distance[i])
