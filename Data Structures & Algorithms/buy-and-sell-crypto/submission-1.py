class Solution:
    """
    Explore:

    prices = [10,1,5,6,7,1]
    6, bc you can buy when it's 1 and sell when it's 7

    prices = [10,8,7,5,2]
    0, bc there's no opportune time to buy as the price goes down

    Brainstorm
     - keep track of the min and keep finding the difference. if new min, switch

    Plan:
        - min_price = prices[0], max_profit = 0

        for price in range(1, prices):
            min_price = min(min_price, price)
            diff = price - min_price
            max_profit = max(max_profit, diff)

        return max_profit
    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        buy_price, max_profit = prices[0], 0

        for sell_price in prices:
            buy_price = min(buy_price, sell_price)
            max_profit = max(max_profit, sell_price - buy_price)

        return max_profit
        
            
     