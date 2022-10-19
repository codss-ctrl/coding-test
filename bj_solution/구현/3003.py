piece = [1,1,2,2,2,8]
nums = list(map(int, input().split(' ')))
l = []
for i in range(len(nums)):
    l.append(piece[i] - nums[i])
print(*l)