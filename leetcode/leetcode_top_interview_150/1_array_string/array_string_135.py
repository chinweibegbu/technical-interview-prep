from typing import List

# Based on understanding from https://youtu.be/1IzCRCcK17A
def candy_optimal(ratings: List[int]) -> int:
    # Set initial values to 1 (settles condition #1)
    candy = [1]*len(ratings)

    # Ensure candy[i] > candy[i-1] if it has a higher rating (settles half of condition #2)
    for i in range(1, len(ratings)):
        if (ratings[i] > ratings[i-1]) and (candy[i] <= candy[i-1]):
            candy[i] = candy[i-1] + 1
    
    # Ensure candy[i] > candy[i+1] if it has a higher rating (settles the other half of condition #2)
    for i in range(len(ratings)-2, -1, -1):
        if (ratings[i] > ratings[i+1]) and (candy[i] <= candy[i+1]):
            candy[i] = candy[i+1] + 1
    
    return sum(candy)