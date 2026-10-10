class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        ans = right

        while left <= right:
            mid = (left + right) // 2
            if self.canSplit(nums, k , mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def canSplit(self, nums: list[int], k: int, target: int) -> bool:
        count = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > target:
                count += 1
                current_sum = num
            else:
                current_sum += num
        
        return count <= k