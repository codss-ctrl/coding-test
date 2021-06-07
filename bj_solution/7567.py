res = 10
a = input()
for i in range(1, len(a)):
   res +=10 if a[i-1] != a[i] else 5
print(res)