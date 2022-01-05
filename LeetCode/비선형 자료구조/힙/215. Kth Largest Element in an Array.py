import heapq


# heapq 모듈 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


# heapq 모듈의 heapify 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums)-k):
            heapq.heappop(nums)

        return heapq.heappop(nums)

# heapq 모듈의 nlargest 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1] # k번째만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴되므로 k번째 값은 -1번째

# 정렬을 이용한 풀이 -> 가장 빠름
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]