# -*- coding: utf-8 -*-
# 브루트 포스 -> 타임아웃
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

       # 브루트 포스 n^3 반복
        for i in range(len(nums)-2):
            # 중복된 값 건너 뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) -1):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j]+nums[k] == 0:
                        result.append([nums[i],nums[j],nums[k]])

# 투 포인터로 합 계산
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)-2):
            # 중복된 값 건너 뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 간격을 좁혀 가며 합 sum 계산
            left, right = i+1, len(nums) -1
            while left < right:
                sum = nums[i]+ nums[left]+nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0 인 경우이므로 정답 및 스킵 처리
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
