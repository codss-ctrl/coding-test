from collections import deque

def bfs():
    q = deque([(hx,hy)])
    while q:
        x,y = q.popleft()
        if abs(px-x)+abs(py-y) <=1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(nx-x)+abs(ny-y) <= 1000:
                    visited[i] = 1
                    q.append((nx,ny))
    print("sad")
    return

t = int(input())
for _ in range(t):
    n = int(input())
    hx,hy = map(int,input().split())
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split())))
    px,py = map(int,input().split())
    visited = [0 for _ in range(n+1)]
    bfs()

