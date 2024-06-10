from typing import List

def maxProfit(prices: List[int]) -> int:
    # Initialise buy and sell days to day 0 and 1, respectively
    l, r = 0, 1
    totalProfit = 0
    
    # Continue until the end of the array
    while (r < len(prices)):
        # Add the difference between the current buy-sell days to the total profit if they are valid
        # NOTE: valid = buy day is less than sell day
        if (prices[l] < prices[r]):
            totalProfit += (prices[r]-prices[l])
        l, r = r, r+1
        
    # Return the total profit
    return totalProfit