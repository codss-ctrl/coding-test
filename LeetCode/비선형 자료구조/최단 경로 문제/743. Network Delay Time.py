# 다익스트라 알고리즘 구현

# 판별사항
# 1. 모든 노드가 신호를 받는 데 걸리는 시간 -> 가장 오래 걸리는 노드까지의 최단 시간 -> 다익스트라
# 2. 모든 노드에 도달할 수 있는지 여부 -> 모든 노드의 다익스트라 알고리즘 계산 값이 존재하는지 유무
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요시간, 정점)]
        Q = [(0, k)]  # 초깃값은 시작점 K부터,소요시간 0
        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)  # 큐 순회 시작하자마자 최솟값 추출
            if node not in dist:  # dist에 node 포함 여부 체크
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1
