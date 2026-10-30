class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        answer = []
        for num in set_1:
            if num in set_2:
                answer.append(num)
        return answer
        