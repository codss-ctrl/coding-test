import sys

n = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
same = [[0]*n for _ in range(n)]
for k in range(5): # 학년
    for i in range(n): # 학생 i
        for j in range(i+1,n): # 학생 j
            if arr[i][k] == arr[j][k]:
                same[i][j]=1
                same[j][i]=1
cnt = []
for i in same:
    cnt.append((i.count(1)))
print(cnt.index(max(cnt))+1)