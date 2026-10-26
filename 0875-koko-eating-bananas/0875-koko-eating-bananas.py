import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # i think KOKO can eat h mount an hour, and Guards are going out for h hours
        
        # Koko wanted to eat all
        
        # Once Koko finishes pile, Koko doesnt want to eat more at the same hour

        # our goal is amount of Koko eat at the same time. 

        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            mid = (left + right) // 2

            hours_taken = sum(math.ceil(pile / mid) for pile in piles)

            # hours taken more than arrival 
            if hours_taken > h:
                left = mid + 1
            else:
                answer = mid
                right = mid - 1
        return answer
