class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        answer = []

        for idx in range(len(nums)):
            if nums[idx] == target:
                answer.append(idx)

        return answer