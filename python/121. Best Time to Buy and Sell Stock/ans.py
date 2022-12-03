class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        best_start_day = 0
        best_end_day = 0
        current_end_day = 0
        while current_end_day != len(prices):
            day_profit = prices[current_end_day] - prices[best_start_day]
            if day_profit > current_profit:
                best_end_day = current_end_day
            elif prices[current_end_day] < prices[best_start_day]:
                best_start_day = current_end_day
            current_profit = max(current_profit, day_profit)
            current_end_day += 1
        return current_profit

