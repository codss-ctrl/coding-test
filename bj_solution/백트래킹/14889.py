import sys

def dfs(cnt, idx):
    global res
    if cnt == n//2:
        star = 0
        link = 0
        for i in range(n):
            for j in range(i+1,n):
                if visited[i] and visited[j]:
                    star += arr[i][j] + arr[j][i]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j] + arr[j][i]
        res = min(res, abs(star-link))
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1,i+1)
            visited[i] = 0
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = 1e9
visited = [0]*n
dfs(0,0)
print(res)