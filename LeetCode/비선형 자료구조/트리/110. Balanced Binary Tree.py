# 재귀 구조로 높이 차이 계산
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0

            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or \
                    right == -1 \
                    abs(left - right) > 1:
                return -1
            return max(left, right) + 1 # 맨 마지막 노드에 이르면 left=0, right=0을 리턴
        # left, right 모두 0이라면 차이가 1보다 크지 않으므로 max(left, right) + 1 리턴

        return check(root) != -1