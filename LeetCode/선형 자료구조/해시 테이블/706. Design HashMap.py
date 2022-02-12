# 개별 체이닝 방식을 이용한 해시 테이블 구현
import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# 풀이 다시 가져옴
# 아래는 discuss에 있던 비슷한 풀이법

class EmptyValue:
    """ For storing empty value """
    pass


class LLNode:
    """ Node of linked list """

    def __init__(self, key: int, val: int, next: Optional['LLNode'] = None) -> None:
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.empty = EmptyValue()
        self.size = 2069
        self.data = [self.empty] * self.size

    def _get_index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._get_index(key)
        if self.data[index] is self.empty:
            self.data[index] = LLNode(key, value)
        else:
            node = self.data[index]
            while node:
                if node.key == key:
                    node.val = value
                    return
                node = node.next
            self.data[index] = LLNode(key, value, self.data[index])

    def get(self, key: int) -> int:
        index = self._get_index(key)
        if self.data[index] is not self.empty:
            node = self.data[index]
            while node:
                if node.key == key:
                    return node.val
                node = node.next
        return -1

    def remove(self, key: int) -> None:
        index = self._get_index(key)
        if self.data[index] is not self.empty:
            prev = None
            node = self.data[index]
            while node:
                if node.key == key:
                    if prev:
                        prev.next = node.next
                    else:
                        self.data[index] = node.next or self.empty
                    return
                prev = node
                node = node.next