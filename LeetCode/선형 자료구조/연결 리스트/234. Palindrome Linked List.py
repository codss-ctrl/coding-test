# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 리스트 변환
import collections


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return False
        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            # 동적 배열 리스트의 첫번째 아이템 추출 속도 문제
            # 첫 번째 값을 꺼내오면 모든 값이 한 칸씩 shifting되며, O(n) 발생
            if q.pop(0) != q.pop():
                return False
        return True

# 데크를 이용한 최적화
# 이중 연결 리스트인 데크는 양쪽 방향 모두 추출하는 데 O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()

        if not head:
            return False
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) >1:
            if q.popleft() != q.pop():
                return False
        return True

# 런너(Runner)를 이용한 풀이
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None # rev : 역순 연결 리스트
        slow = fast = head # 모두 head에서 시작
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next # 빠른 런너는 2칸씩
            rev, rev.next, slow = slow, rev, slow.next # 느린 런너는 1칸씩 이동
            # rev는 None에서 시작하고, 런너가 이동하면서 1->None, 2->1->None로 점점 이전 값으로 연결되는 구조
            # 현재 값을 slow로 교체하고, rev.next는 rev가 됨. -> 앞에 계속 새로운 노드가 추가되는 형태

        # 입력값이 홀수 일 때 중앙에 위치한 값이 팰린드롬 체크에서 배제되어야 하기 때문. -> fast가 아직 None이 아니라는 경우로 간주할 수 있다.
        if fast:
            slow = slow.next  # -> slow를 한 칸 더 이동해 마무리


        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:  # 역순으로 만든 연결 리스트 rev 반복
            slow, rev = slow.next, rev.next  # slow의 나머지 이동 경로와 역순으로 만든 rev의 노드를 하나씩 풀어가면서 비교
            # 정상적으로 비교가 종료됐다면 slow와 rev가 모두 끝까지 이동해 둘 다 None이 된다.

        return not rev  # 최종결과는 return not rev 또는 return not slow