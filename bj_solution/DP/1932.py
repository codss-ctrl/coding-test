n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
# 모서리의 수들은 바로 윗값을 더하여 저장. 그 외의 수들은 대각선의 값 중 max 값 더해서 저장
for i in range(1,n):
    for j in range(len(arr[i])):
        if j ==0:
            arr[i][j] = arr[i][j]+arr[i-1][j]
        elif j == len(arr[i])-1:
            arr[i][j] = arr[i][j]+arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i-1][j],arr[i-1][j-1])+arr[i][j]
print(max(arr[-1]))