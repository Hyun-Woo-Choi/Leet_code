class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        
        # k가 전체 일수의 절반 이상이면 거래 횟수 제한이 무의미함 (단순 그리디)
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

        # buy[j]: j+1번째 주식을 샀을 때의 최대 잔고
        # sell[j]: j+1번째 주식을 팔았을 때의 최대 잔고
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                # j번째 매수: 이전(j-1번째) 매도 수익에서 현재 주가를 뺌
                buy[j] = max(buy[j], sell[j - 1] - price)
                # j번째 매도: j번째 매수 상태에서 현재 주가를 더함
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k]