a = input()
pal = 1
for i in range(len(a)//2): # 0부터 문자열 길이의 절반만큼 반복
    if a[i] == a[-1-i]:
        pass
    else: pal =0
print(pal)
