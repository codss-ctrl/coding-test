import sys

input = sys.stdin.readline
n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
mincost = cost[0]
total = 0
for i in range(n-1):
    if mincost > cost[i]:
        mincost = cost[i]
    total += mincost * dist[i]
print(total)

