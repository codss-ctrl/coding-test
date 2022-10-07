import sys


def dfs(depth, idx):
    global min_diff
    if depth == N//2:
        start, link = 0,0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        min_diff = min(min_diff, abs(start - link))
        return

        for i in range(idx, N):
            if not visited[i]:
                visited[i] = True
                dfs(depth+1, i+1)
                visited[i] = False

input = sys.stdin.readline
N = int(input())
visited = [False] * N
graph = [list(map(int, input().split())) for _ in range(N)]
min_diff = 1e9

dfs(0,0)
print(min_diff)