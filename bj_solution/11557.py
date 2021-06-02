n = int(input())  # 테스트 케이스 개수 n
for _ in range(n):  # n개의 케이스 동안
    t = int(input())  # 학교수 t
    data = dict()  # 학교 : 술 담을 dict 객체 생성
    for _ in range(t):  # 학교수 t 동안
        a, b = input().split()  # 학교명은 a에, 술 양은 b에 담음
        data[a] = int(b)  # data[key] = value 구조로 저장, 술 양은 int로 형변환
        reverse_data = dict(map(reversed, data.items()))  # dict의 key와 value 위치를 바꿈
        # reverse_data 의 구조는 {술양 : 학교명} 상태
        # key(술양) 중 가장 큰 값(max) 구하고, key를 arg로 사용해서 value인 학교명 꺼내서 출력
    print(reverse_data.get(max(reverse_data.keys())))
