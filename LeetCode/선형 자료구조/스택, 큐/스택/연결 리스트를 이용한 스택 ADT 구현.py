# 연결 리스트를 이용한 스택 ADT 구현

class Node:
    def __init__(self, item, next):
        self.item = item  # 노드의 값
        self.next = next  # 다음 노드를 가리키는 포인터


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item  # 요소 추가
        self.last = self.last.next  # 가장 마지막 값 next로 지정, last 포인터를 한 칸 앞으로 전진
        return item
