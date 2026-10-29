"""
    Problem: 
        hold only one stock, you can buy and sell at the same day,
        multiple times would be possible. 
        maxmize the profit
    intution:
        buy stock -> sell only when its expensive than holding stock 
    algo:
        Greedy 
        from first,
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for idx in range(len(prices)-1):
            if prices[idx+1] > prices[idx]:
                profit += prices[idx+1] - prices[idx]
        
        return profit