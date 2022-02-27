# 브루트 포스로 계산
import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))

        return r


# 큐를 이용한 최적화
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')  # 음의 무한대로 설정
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue
            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최댓값이 윈도우에서 빠지면 최대화
            if current_max == window.popleft():
                current_max = float('inf')
        return results


# 테스트 케이스 변경으로 위 두개는 타임 오류
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, ans = collections.deque(), []

        for i in range(len(nums)):
            # 앞에서부터 out of window -> 제거
            if deq and i-deq[0] == k:
                deq.popleft()

            # 뒤에서부터 현재 추가할 숫자보다 작으면 -> 제거 (deq에 불필요한 숫자 없도록!)
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()

            deq.append(i) # 현재 숫자 추가( (i, num[i])로 저장해도 되나, 숫자 위치 저장만 해 space 줄임)

            # 출력 부분 (현재 위치 >= window size일 때)
            if i+1 >= k:
                ans.append(nums[deq[0]])  # 맨 앞은 현재 window 에서 가장 큰 수

        return ans

sol = Solution()
print(sol.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3))
