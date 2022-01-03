# 배열을 이용한 풀이
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0  # front 포인터
        self.p2 = 0  # rear 포인터

    def enQueue(self, value: int) -> bool:  # rear 포인터 이동
        if self.q[self.p2] is None:
            self.q[self.p2] = value  # rear 포인터 p2 위치에 값을 넣는다
            self.p2 = (self.p2 + 1) % self.maxlen  # 포인터를 한 칸 앞으로 이동
            # 전체 길이만큼 모듈로(나머지) 연산을 하여 포인터의 위치가 전체 길이를 벗어나지 않게 함
            # 만약 rear 포인터 위치가 None이 아니라면 다른 요소가 있는 공간이 꽉 찬 상태이거나 비정상적인 경우이므로 False 리턴
            return True
        else:
            return False

    def deQueue(self) -> bool:  # front 포인터 이동
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None  # front 포인터 p1의 위치에 None을 넣어 삭제를 하고
            self.p1 = (self.p1 + 1) % self.maxlen  # 포인터를 한 칸 앞으로 이동하면서 최대 길이를 넘지 않도록 한다.
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:  # 원래 큐에는 Rear() 연산이 없음
        return -1 if self.q[self.p2] is None else self.q[self.p2]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.p1[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.p1[self.p1] is not None
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
