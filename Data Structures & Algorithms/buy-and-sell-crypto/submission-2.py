class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        i=0
        for j in range(1,len(prices)):
            if prices[i]>prices[j]:
                i = j
            max_profit=max(max_profit,prices[j]-prices[i])
        return max_profit