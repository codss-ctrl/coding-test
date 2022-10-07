import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
s = 0
for i in range(n):
    s += max(a) * min(b)
    a.pop(a.index(max(a)))
    b.pop(b.index(min(b)))
print(s)