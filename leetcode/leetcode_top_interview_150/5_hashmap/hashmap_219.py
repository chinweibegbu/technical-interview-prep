from collections import defaultdict
from typing import List

def containsNearbyDuplicate_intial(nums: List[int], k: int) -> bool:
    tracker = defaultdict(list)
    for i, num in enumerate(nums):
        if (num in tracker):
            if (abs(i - tracker[num][-1]) <= k):
                return True
        tracker[num].append(i)
    return False

def containsNearbyDuplicate_solution(nums: List[int], k: int) -> bool:
    # Create a dictionary which, by default, sets each value to an array
    tracker = defaultdict(list)

    # For each index and num in nums
    for i, num in enumerate(nums):
        # If num is in tracker and the difference between its last occurence and i <= k, return True
        if ((num in tracker) and (abs(i - tracker[num][-1]) <= k)):
            return True
        # Add i to the array of indices for num in the dictionary
        tracker[num].append(i)
            