k = int(input())
choco = 1
while choco < k:
    choco = choco<<1
cnt = 0
c = choco
while k > 0:
    if k >= c:
        k -= c
    else:
        c = c//2
        cnt +=1
print(choco,cnt)