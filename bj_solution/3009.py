import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

if y2 == y3:
    y4 = y1
elif y1 == y2:
    y4 = y3
elif y3 == y1:
    y4 = y2

if x3 == x2:
    x4 = x1
elif x3 == x1:
    x4 = x2
elif x1 == x2:
    x4 = x3
print(x4, y4)
