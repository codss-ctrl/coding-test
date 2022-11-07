import heapq
import sys

n = int(input())
q = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(q,(abs(a),a))
    else:
        try:
            print(heapq.heappop(q)[1])
        except:
            print(0)