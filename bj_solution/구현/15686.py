import sys
from itertools import combinations

input = sys.stdin.readline
n,m = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
chick = []
house = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            chick.append((i,j))
        if maps[i][j] == 1:
            house.append((i,j))

ans = 1e9
combi = combinations(chick,m)
for c in combi:
    total = 0
    for h in house:
        dis = 1e9
        for x,y in c:
            dis = min(dis,abs(h[0]-x) + abs(h[1]-y))
        total += dis
    ans = min(ans,total)
print(ans)




