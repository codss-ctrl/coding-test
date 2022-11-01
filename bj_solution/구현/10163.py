n = int(input())
arr = [[0]*1001 for _ in range(1001)]
for k in range(1,n+1):
    x,y,w,h = map(int, input().split())
    for i in range(x,x+w):
        for j in range(y,y+h):
            arr[i][j] = k
color = [0]*(n+1)
for i in range(1001):
    for j in range(1001):
        if arr[i][j]:
            color[arr[i][j]] += 1
for i in range(1,n+1):
    print(color[i])