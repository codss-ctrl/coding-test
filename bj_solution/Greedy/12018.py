n,m = map(int, input().split())
cnt = 0
res = []
for _ in range(n):
    p,l = map(int,input().split())
    mileage = list(map(int, input().split()))
    mileage.sort(reverse=True)
    if l > p:
        res.append(1)
    else:
        res.append(mileage[l-1])
res.sort()
for i in res:
    m -= i
    cnt += 1
    if m < 0:
        print(cnt-1)
        break
if m > 0:
    print(cnt)