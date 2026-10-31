"""
    problem: given sorted list of int, we have to return smallest sorted list. 

"""

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            # advance as long as next number is consecutive till i is less then len(nums)
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}")
            else:
                ans.append(f"{start}")
            i += 1
        return ans

