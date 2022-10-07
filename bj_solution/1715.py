import heapq
import sys

input = sys.stdin.readline
N = int(input())
card = []
for _ in range(N):
    heapq.heappush(card, int(input()))
if len(card) == 1:
    print(0)
else:
    ans = 0
    while len(card) > 1:
        num1 = heapq.heappop(card)
        num2 = heapq.heappop(card)
        ans += num1 + num2
        heapq.heappush(card, num1+num2)
    print(ans)