import itertools

n,m = map(int, input().split(' '))
p = itertools.combinations_with_replacement(range(1,n+1),m)
for i in p:
    print(*i, sep=' ')