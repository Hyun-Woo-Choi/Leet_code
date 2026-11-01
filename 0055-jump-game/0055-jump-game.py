class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        curr_pos = 0

        while nums[curr_pos] > 0:
            max_reach = 0
            best_next_pos = curr_pos

            for next_pos in range(curr_pos+1, min(len(nums), curr_pos + nums[curr_pos] + 1)):

                if next_pos >= len(nums) - 1:
                    return True
                
                reach = next_pos + nums[next_pos]

                if reach >= len(nums) - 1:
                    return True
                
                if reach > max_reach:
                    max_reach = reach
                    best_next_pos = next_pos
            
            if best_next_pos == curr_pos:
                return False
            
            curr_pos = best_next_pos
        
        return False