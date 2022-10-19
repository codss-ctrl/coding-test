from collections import Counter
import sys

s = sys.stdin.readline().strip().upper()
if len(s) == 1:
    print(s)
    exit(0)
c = Counter(s)
tmp = c.most_common(2)
if tmp[0][1] == tmp[1][1]:
    print('?')
else:
    print(tmp[0][0])
