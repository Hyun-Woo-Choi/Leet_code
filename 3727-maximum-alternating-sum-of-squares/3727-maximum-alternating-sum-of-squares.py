from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # 각 원소의 제곱을 구한 뒤 오름차순 정렬
        squares = sorted(x * x for x in nums)
        
        n = len(nums)
        half = n // 2
        
        # 작은 half개는 빼고, 큰 나머지는 더함
        return sum(squares[half:]) - sum(squares[:half])