# Two Pointers Solution
# Time O(n)
class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start <= end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start+1, end+1]
            elif sum < target:
                start +=1
            else:
                end -= 1

# Binary Search Solution
# Time 0(nlogn)
class Solution2:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        for idx in range(len(numbers)): #0(n)
            new_target = target-numbers[idx]
            left, right = idx +1, len(numbers) -1
            while left <= right: #0(nlogn)
                mid = left + (right-left)//2
                if numbers[mid] == new_target:
                    return [idx+1, mid+1]
                elif numbers[mid]>new_target:
                    right = mid-1
                else:
                    left = mid+1
