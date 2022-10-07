n = int(input())
n = 1000 - n
coin = [500,100,50,10,5,1]
cnt = 0
for c in coin:
    cnt += n//c
    n %= c
print(cnt)