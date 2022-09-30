# def dfs(stack, start, n, m):
#     if len(stack) == m:
#         print(*stack, sep=' ')
#         return
#     for i in range(1,n+1):
#         stack.append(i)
#         dfs(stack,i,n,m)
#         stack.pop()
# n,m = map(int, input().split(' '))
# dfs([],1,n,m)

import itertools

n,m = map(int, input().split(' '))
p = itertools.product(range(1,n+1),repeat=m)
for i in p:
    print(*i, sep=' ')
