class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answer = []

        def backtrack(start, path, current_sum):

            if current_sum == target:
                answer.append(list(path))
                return
            
            if current_sum > target:
                return 
            
            for i in range(start, len(candidates)):
                num = candidates[i]

                path.append(num)

                backtrack(i, path, current_sum + num)

                path.pop()
        backtrack(0, [], 0)
        return answer
        