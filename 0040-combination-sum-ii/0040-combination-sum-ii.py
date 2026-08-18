class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()


        def backtracking(start: int, path: List[int], total_sum:int):
            if total_sum == target:
                answer.append(path.copy())
                return 

            if total_sum > target:
                return 

            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i -1]:
                    continue

                if total_sum + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtracking(i + 1, path, total_sum + candidates[i])
                path.pop()

        backtracking(0, [], 0)
        return answer