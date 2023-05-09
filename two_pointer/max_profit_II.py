class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit += prices[r] - prices[l]
            l = r
            r += 1


        return profit
