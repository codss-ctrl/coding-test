n = int(input())
cy = sd = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        sd -= a
    elif a ==b:
        pass
    else:
        cy -= b
print(cy)
print(sd)