# 이중 연결 리스트를 이용한 데크 구현
class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0  # 최대 길이 정보 k, 현재 길이 정보 len
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:  # 최대 길이에 도달했을때 false
            return False
        self.len += 1
        self._add(self.head, ListNode(value))  # head 위치에 노드 삽입
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:  # 최대 길이에 도달했을때 false
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))  # tail 위치에 노드 삽입
        return True

    def deleteFront(self) -> bool:
        if self.len == self.k:  # 최대 길이에 도달했을때 false
            return False
        self.len -= 1
        self._del(self.head)

    def deleteLast(self) -> bool:
        if self.len == self.k:  # 최대 길이에 도달했을때 false
            return False
        self.len -= 1
        self._del(self.tail.left.left)

    def getFront(self) -> int:
        return self.head.left.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
