class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        

        while left <= right:

            mid = (left + right) // 2
            # find the target at mid
            if nums[mid] == target:
                return mid
            # if left part is ascending order
            if nums[left] <= nums[mid]:
                # if target is in the left part
                if nums[left] <= target < nums[mid]:
                    right = mid  -1
                # not in the left part, move to right part
                else:
                    left = mid + 1
            # right part is ascending order (since left is not)
            else: 
                # if target is in the right part -> search right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # not in the right part -> search left
                else:
                    right = mid - 1
        
        return -1