class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return [-1]
        n = len(nums)
        answer = [-1] * n
        stack = []

        for idx in range(2 * n):

            curr_idx = idx % n
            curr_num = nums[curr_idx]

            """
                [1,2,1,2,1,2]
                [1,2,3,4,5,6]
                [5,4,3,2,1]
                [1,1,1,1,1]

            """
            while stack and nums[stack[-1]] < curr_num :
                prev_num = stack.pop()
                answer[prev_num] = curr_num
            
            if idx < n:
                stack.append(curr_idx)
        
        return answer