from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        num_dict = defaultdict(int)
        for num in nums:
            if num_dict[num] == 1:
                return num
            else:
                num_dict[num] = 1
