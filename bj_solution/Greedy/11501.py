t = int(input())
for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    max = 0
    value = 0
    for i in range(n-1,-1,-1):
        if stocks[i] > max:
            max = stocks[i]
        else:
            value += max - stocks[i]
    print(value)