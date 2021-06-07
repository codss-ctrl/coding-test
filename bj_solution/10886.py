n = int(input())
res1=res0= 0
for _ in range(n):
    a = int(input())
    if a==1:
        res1+=1
    else: res0+=1
if res1 > res0:
    print("Junhee is cute!")
else:print("Junhee is not cute!")
