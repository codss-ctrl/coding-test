# 삽입 정렬
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 문제에 적합한 비교 함수
        @staticmethod
        def to_swap(n1: int, n2:int)->bool:
            return str(n1)+ str(n2) <str(n2)+str(n1)

        # 삽입 정렬 구현
        def largestNumber(self, nums:List[int]) -> str:
            i=1
            while i<len(nums):
                j = i
                while j>0 and self.to_swap(nums[j-1], nums[i]):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j -= 1
                i += 1

            return str(int(''.join(str, nums))) # ["0","0"] 같은 경우도 있기때문에 00이 0이 되도록 만들어 준 후, 다시 str로 변경한다
