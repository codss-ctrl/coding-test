n = int(input())
res = 0
expect = []
for _ in range(n):
    expect.append(int(input()))
expect.sort()
for i in range(n):
    res += abs(i+1 - expect[i])
print(res)