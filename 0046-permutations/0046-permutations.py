class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtracking(current_path, remaining):
            if not remaining:
                ans.append(current_path)
                return
            
            for i in range(len(remaining)):
                backtracking(current_path + [remaining[i]], remaining[:i] + remaining[i+1:])
        backtracking([], nums)
        return ans 