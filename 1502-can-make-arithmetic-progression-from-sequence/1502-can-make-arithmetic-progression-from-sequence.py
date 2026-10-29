class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        if not arr or len(arr) < 2:
            return False

        diff = arr[1] - arr[0]

        for idx in range(2,len(arr)):
            if arr[idx] - arr[idx-1] != diff:
                return False
        
        return True