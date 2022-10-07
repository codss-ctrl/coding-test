import sys

input = sys.stdin.readline
s = input().strip()
one = s.split('0')
zero = s.split('1')
one_cnt = 0
zero_cnt = 0
for o in one:
    if o:
        one_cnt+=1
for z in zero:
    if z:
        zero_cnt += 1
if one_cnt == 0 or zero_cnt == 0:
    print(0)
elif one_cnt > zero_cnt:
    print(zero_cnt)
else:
    print(one_cnt)
