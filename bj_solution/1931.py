import sys


input = sys.stdin.readline
n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().split())))
times.sort(key=lambda x: (x[1],x[0]))
cnt = 0
current = 0
for time in times:
    if time[0] >= current:
        cnt += 1
        current = time[1]
print(cnt)