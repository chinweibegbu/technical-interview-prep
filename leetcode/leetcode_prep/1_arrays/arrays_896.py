"""
Thoughts:
    This algorithm has a runtime of O(n).
    Traversal through the array is an O(n) operation while comparison and swapping are both O(1) operations.
"""

from typing import List

def isMonotonic(self, nums: List[int]) -> bool:
    # Set up monotonic order (increasing or decreasing)
    isDecreasing = False
    for i in range(0, len(nums)-1):         # Continue until first switch
        if (nums[i] != nums[i+1]):
            isDecreasing = True if (nums[i] >= nums[i+1]) else False

    # Traverse until expected order is broken
    for i in range(1, len(nums)-1):
        if ((nums[i-1] <= nums[i]) and (nums[i] <= nums[i+1])) and (not isDecreasing):
            continue
        elif ((nums[i-1] >= nums[i]) and (nums[i] >= nums[i+1])) and (isDecreasing):
            continue
        else:
            return False
    
    # If expected order is never broken, it is monotonic
    return True