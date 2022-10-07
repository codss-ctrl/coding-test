import sys

cnt = 1
while True:
    l, p, v = map(int,sys.stdin.readline().strip().split())
    if l == p == v == 0:
        break
    ans = l * (v // p) + min(l, v % p)
    print(f'Case {cnt}: {ans}')
    cnt += 1
