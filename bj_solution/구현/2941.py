import re
import sys

strs = sys.stdin.readline().strip()
cnt = 0
s=re.sub("c=|c-|dz=|d-|lj|nj|s=|z=",'-',strs)
print(len(s))
# l,r = 0,1
# while l <= r <= len(strs):
#     if strs[l:r+1] not in dic:
#         if r - l == 2:
#             l += 1
#             cnt += 1
#         else:
#             r += 1
#     else:
#         l = r + 1
#         r = l + 1
#         cnt += 1
# print(cnt)
