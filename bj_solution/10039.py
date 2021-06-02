list1 = []  # 점수 담을 리스트 생성
for _ in range(5):  # 5개의 점수를 줄마다 받아야하므로 반복문 사용
    list1.append(int(input()))  # list에 추가
for i in range(len(list1)):  # list 길이만큼 돌면서
    if list1[i] < 40:  # 점수가 40점 미만이면
        list1[i] = 40  # 값을 40점으로 바꿈

print((sum(list1))//5)  # 총합 구하고 5로 나눔


