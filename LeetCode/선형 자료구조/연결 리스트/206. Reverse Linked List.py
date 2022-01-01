# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 재귀 구조로 뒤집기
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev  # node.next에는 이전 prev 리스트를 계속 연결하면서 node가 None이 될 때까지 재귀 호출하면 마지막에는 백트래킹되면서 연결 리스트가 거꾸로 연결
            # 맨 처음에 리턴된 prev는 뒤집힌 연결 리스트의 첫 번째 노드가 된다.
            return reverse(next, node) # 노드 next와 현재 노드를 파라미터로 지정한 함수를 재귀 호출
        return reverse(head)

# 반복 구조로 뒤집기 -> 공간 복잡도가 더 낮음
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev