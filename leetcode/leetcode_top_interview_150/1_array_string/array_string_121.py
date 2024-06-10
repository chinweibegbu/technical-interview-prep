from typing import List

def maxProfit_FAILED(prices: List[int]) -> int:
    n = len(prices)

    # Edge case: List has less than 2 elements/days
    if (n < 2): return 0

    # Store max profit for each possible buy day in an array
    profits = []
    
    # Iterate until the second to last element/day
    # WHY? Because you can't sell if you buy on the last day
    for i in range(n-1):
        # Calculate the maximum profit of the current element/day
        profit = max(prices[(i+1):]) - prices[i]
        
        # Add the profit or 0 for the current element/day to the store array if its greater than 0 or not, respectively
        profits.append(profit if profit>0 else 0)
    
    # Return the maximum calculated profit
    return max(profits)


# Based on understanding of https://www.youtube.com/watch?v=1pkOgXD63yU
def maxProfit_optimal(prices: List[int]) -> int:
    # Initialise buy and sell days to day 0 and 1, respectively
    l, r = 0, 1
    maxProfit = 0
    
    # Continue while there are valid sell days
    while (r < len(prices)):
        # If the buy day's price is greater than the sell day's price, update buy and sell date
        if (prices[l] > prices[r]):
            l, r = r, r+1
        # Else, set maxProfit to the larger of the buy and sell days (with valid relative prices) and update the sell day
        else:
            maxProfit = max(maxProfit, (prices[r]-prices[l]))
            r += 1
    
    # Return maxProfit
    return maxProfit