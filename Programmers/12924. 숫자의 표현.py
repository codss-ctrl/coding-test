def solution(n):
    answer = 0
    a = 1 # 등차수열의 a (첫째항)
    d = 1 # 등차수열의 공차
    while a <= n: # 첫째항은 n까지 가능
        b = a # 공차 d마다 수열을 계산할 예비 첫째항 b를 선언
        while b <= n:
            if b == n:
                answer += 1
                break
            b += d
        d += 1 # 등차 1,2,3,4...순으로 증가
        a += d # 첫째항에 등차를 더해 첫째항 갱신 1,3,6,10...
    return answer