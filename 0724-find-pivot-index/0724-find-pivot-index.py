"""
    Problem: we need to pick a index, 
            left sum == right sum 
            if the index = 0, means left sum is 0
            if the index = len(nums) - 1, means right sum is 0

    idea: sum of left and right should be equal. 

    Q. is array sorted - No

    1. Pivot index not included in calculation. 

    Intuition: Actually my first intention was doing binary search, but the arrya is not sorted. we will skip that one.
        we need to do the Brute force, checking every index from beginig .
"""

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)

        left_sum = 0

        for idx, num in enumerate(nums):
            if left_sum == total_sum - num - left_sum:
                return idx
            left_sum += num
        
        return -1