import re
import sys

r,c = map(int, input().split())
res = [-1]*9
for _ in range(r):
    strs = sys.stdin.readline().strip()
    S = re.split('[1-9]{2}', strs)
    if S[0].count('.') != (c-2):
        res[int(S[1][0])-1] = c-5 - S[0].count('.')

dict = {}
rank = 1
for num in sorted(res):
    if num not in dict:
        dict[num] = rank
        rank += 1
rank_list = [dict[i] for i in res]
for i in rank_list:
    print(i)
