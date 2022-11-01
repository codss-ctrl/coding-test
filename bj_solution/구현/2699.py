import sys

graph = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            graph[x][y] += 1
res = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] != 0:
            res += 1
print(res)