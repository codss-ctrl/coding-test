notes = list(map(int, input().split(' ')))
asc = False
des = False
for i in range(1,len(notes)):
    if notes[i] == notes[i-1] + 1:
        asc = True
    elif notes[i] == notes[i-1] - 1:
        des = True
    else:
        asc = False
        des = False
        break

if asc is True:
    print("ascending")
elif des is True:
    print("descending")
else:
    print("mixed")