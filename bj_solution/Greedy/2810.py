n = int(input())
seat = input()
count = seat.count('LL')
if count <= 1:
    print(n)
else:
    print(n-count+1)
