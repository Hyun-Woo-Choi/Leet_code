class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        visited = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                
                visited[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                visited[i] = False
        backtrack([])
        return res