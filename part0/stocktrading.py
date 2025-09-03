
def maxProfit(prices):
  maxProfit= 0
  minBuy = 10000000

  for i in prices:
    if price [i] < minBuy: 
      minBuy = price[i]
    if price[i]-minBuy > maxProfit:
      maxProfit = price[i]-minBuy

print("Return value: ", maxProfit)
