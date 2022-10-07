import sys

n = list(sys.stdin.readline().strip())

n.sort(reverse=True)
ans = 0
if int(''.join(n)) % 30 == 0:
    print(int(''.join(n)))
else:
    print(-1)
