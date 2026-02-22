class Solution(object):
    def max_profit(self, prices):
        min_price = float('inf')
        max_profit = float('-inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == "__main__":
    raw = input("enter daily prices: ")
    prices = list(map(int, raw.strip().split()))
    sol = Solution()
    result = sol.max_profit(prices)
    print("Maximum profit:", result)