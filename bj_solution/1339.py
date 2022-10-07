import collections
import sys
N = int(sys.stdin.readline())

res = 0
strs = []
nums = []
kind = set()
dic = collections.defaultdict(int)
for _ in range(N):
    strs.append(sys.stdin.readline().strip())
for i in range(N):
    for j in range(len(strs[i])):
        dic[strs[i][j]] += 10**(len(strs[i])-j-1)
for val in dic.values():
    nums.append(val)
nums.sort(reverse=True)
pows = 9
ans = 0
for i in nums:
    ans += i * pows
    pows-=1
print(ans)