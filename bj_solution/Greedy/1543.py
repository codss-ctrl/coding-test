strs = input()
target = input()
now = 0
cnt = 0
while now < len(strs):
    if target == strs[now:now+len(target)]:
        cnt += 1
        now += len(target)
    else:
        now += 1
print(cnt)