k, n, m = map(int, input().split());print(max(0,k*n-m))

k, n, m = map(int, input().split()) # 입력
if k * n <= m: # 과자 총액보다 돈 많으면
    print(0)  # 돈을 더 받지 않는다
else: # 총액보다 돈이 없다면
    print(k*n - m) # 부족한 만큼 돈을 더 받는다