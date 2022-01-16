# 삽입 정렬
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < had.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            cur = parent

        return cur.next

# 삽입 정렬의  비교 조건 개선
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < had.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리리
           if head and cur.val > head.val:
                cur = parent

        return cur.next