N,L = map(int, input().split())
pool = [list(map(int,input().split())) for _ in range(N)]
pool.sort()
now = pool[0][0]
total = 0
for start,end in pool:
    if now > end:
        continue
    elif now < start:
        now = start
    dist = end - now
    remain = 1
    if dist % L == 0:
        remain = 0
    cnt = dist//L + remain
    now += cnt * L
    total += cnt
print(total)