# 정수 N, M를 입력받기
n, m = map(int,input().split())
# N개의 화폐 단위 정보를 입력받기
list = []
for i in range(n):
    list.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 보텀업
d[0] = 0
d[min(list)] = 1
for i in range(min(list), m+1):
    for money in list:
        # 음수가 되면 중단한다
        if i - money < 0:
            break
        else:
            d[i] = min(d[i], d[i-money]+1) # 최솟값 갱신

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
