
def maxProfit(prices):
    maxProfit= 0
    minBuy = 10000000
    
    for i in range(len(prices)):
        if prices[i] < minBuy: 
          minBuy = prices[i]
        if prices[i]-minBuy > maxProfit:
          maxProfit = prices[i]-minBuy
    
    print("Return value: ", maxProfit)

