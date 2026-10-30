"""
    problem: from the list, we need to make subarray that greater or equeal to the target

    things we need to consider: 
        it can have same subarray at the same time. but we only need the minimum legnth 
    
    then how should we make a subarray?
    -> my first intuition is DP or BFS

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float("inf")
        
        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
            
        return min_len if min_len != float("inf") else 0