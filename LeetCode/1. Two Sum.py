# 브루트 포스
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

# in을 이용한 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            complement = target - v

            if complement = in nums[i+1:]:
            return [nums.index(v), nums[i + 1:].index(complement) + (i + 1)]

# 첫 번째 수를 뺀 결과 키 조회
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        #타겟에서 첫번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]

# 조회 구조 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

# 투 포인터 이용 -> 리스트가 정렬되어 있지 않아 풀이 불가
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left]+nums[right] < target:
                right -= 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left]+nums[right] < target:
                left -= 1
            else:
                return [left, right]


