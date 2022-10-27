from collections import deque
n,k = map(int, input().split())
visited = [0]*100001
MAX = 100001
q = deque([n])
while True:
    num = q.popleft()
    if num == k:
        print(visited[k])
        exit(0)
    for i in (num-1,num+1,num*2):
        if 0<=i<MAX and not visited[i]:
            visited[i] = visited[num]+1
            q.append(i)
