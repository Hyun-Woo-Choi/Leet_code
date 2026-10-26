class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        answer = 0
        temp = 0

        for num in nums:
            if num == 1:
                temp += 1
                answer = max(temp, answer)
            else:
                temp = 0
        
        return answer