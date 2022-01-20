# 브루트 포스로 과반수 비교 -> 타임아웃
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num


# 다이나믹 프로그래밍
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num


# 분할 정복
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        a = self.majorityElement(nums[:len(nums) // 2])
        b = self.majorityElement(nums[len(nums) // 2:])

        return [b, a][nums.count(a) > len(nums) // 2]


# 파이썬다운 방식 -> 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
