answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = True
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = False


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [False] * N
    dfs(k, 0, dungeons)
    return answer




k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k,dungeons))
