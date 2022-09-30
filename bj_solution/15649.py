import itertools

n,m = map(int, input().split(' '))
p = itertools.permutations(range(1,n+1),m)
for i in p:
    print(*i, sep=" ")