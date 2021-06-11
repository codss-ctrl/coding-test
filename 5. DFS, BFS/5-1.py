stack = []

# 5 삽입 - 2 삽입 - 3삽입 - 7삽입 - 삭제 - 1 삽입 - 4 삽입 - 삭제
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(7)
stack.pop()
stack.push(1)
stack.push(4)
stack.pop()

print(stack)  # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력
