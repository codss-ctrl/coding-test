n = int(input())
arr = [1]*10
for i in range(n):
    for j in range(1,10):
        arr[j] += arr[j-1]
print(arr[-1]%10007)