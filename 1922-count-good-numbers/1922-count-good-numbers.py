class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7 
        total = pow(20, n // 2, MOD)

        if n % 2 == 1: 
            total = (total * 5) % MOD
        return total