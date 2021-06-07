t = int(input())
for _ in range(t):
    ys = ko = 0
    for _ in range(9):
        y, k = map(int, input().split())
        ys+=y
        ko+=k
    if ys > ko :
        print("Yonsei")
    elif ys == ko:
        print("Draw")
    else:
        print("Korea")