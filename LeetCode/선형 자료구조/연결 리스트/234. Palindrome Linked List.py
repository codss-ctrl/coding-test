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
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev