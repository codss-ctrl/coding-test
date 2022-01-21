# 메모이제이션
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] >0 else 0
        return max(nums)

# 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_num = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_num = max(best_num, current_sum)

        return best_num