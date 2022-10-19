n = input()
# while n:
#     print(n[:10])
#     n = n[10:]
for i in range(0,len(n), 10):
    print(n[i:i+10])