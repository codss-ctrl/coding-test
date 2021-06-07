n = int(input())
Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0
for i in range(n):
    x, y = map(int, input().split())
    if x >0 and y > 0:
        Q1 += 1
    elif y > 0 > x:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 > y:
        Q4 += 1
    elif x == 0 or y == 0:
        AXIS += 1
print("Q1: "+str(Q1))
print("Q2: "+str(Q2))
print("Q3: "+str(Q3))
print("Q4: "+str(Q4))
print("AXIS: "+str(AXIS))

