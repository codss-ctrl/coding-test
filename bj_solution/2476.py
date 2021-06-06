n = int(input())
money = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if a ==b and b ==c :
        money.append(10000+b*1000)
    elif a==b or b == c :
        money.append(1000+b*100)
    elif a ==c :
        money.append(1000+a*100)
    else:
        money.append(max(a, b, c)*100)
print(max(money))