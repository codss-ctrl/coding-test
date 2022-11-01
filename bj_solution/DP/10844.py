import copy

n = int(input())
if n == 1:
    print(9)
    exit(0)
num = [1]*12
num[0] = 0
num[1] = 0
num[-1] = 0
for i in range(n-1):
    tmp = copy.deepcopy(num)
    for j in range(1,11):
        num[j] = tmp[j-1]+tmp[j+1]

for k in range(1, 11):
    num[k] += num[k - 1]
print(num[10]%10**9)
