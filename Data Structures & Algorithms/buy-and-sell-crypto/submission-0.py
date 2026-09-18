class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        cur_profit = 0

        if len(prices) == 1:
            return 0

        while j < len(prices):
            if prices[j] - prices[i] > cur_profit:
                cur_profit = prices[j] - prices[i]

            if prices[i] > prices[j]:
                i += 1
            else:
                j += 1
            
        return max(cur_profit, 0)
        