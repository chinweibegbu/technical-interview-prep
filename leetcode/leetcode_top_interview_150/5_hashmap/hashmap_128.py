from typing import List

def longestConsecutive_initial_FAILED(nums: List[int]) -> int:
    if (len(nums) <= 1): return len(nums)

    tracker = {}
    for num in nums:
        tracker[num] = 1 if (num-1) in tracker else 0
    
    if len(tracker.keys()) == 1: return 1
    
    maximum = min(nums) - 1
    for n in tracker:
        tracker[n] = 1 if (n-1) in tracker else 0
        if (tracker[n] == 1 and n > maximum):
            maximum = n
    
    length = 1
    num = maximum
    while (tracker[num] != 0):
        num = num-1
        length += 1
    
    return length

def longestConsecutive_optimal_1(nums: List[int]) -> int:
    # Edge case: If the list is empty, return 0
    if (len(nums) == 0): return 0
    
    # Get the unique elements in num
    elements = set(nums)

    maxLength = 1
    for num in nums:
        # If it is the beginning of a sequence, get the sequence length and update maxLength
        if (num-1 not in elements):
            number = num
            length = 0
            while number in elements:
                length += 1
                number += 1
            maxLength = max(maxLength, length)
    
    # Return the maximum length
    return maxLength

# Based on code by Neetcode at https://youtu.be/P6RZZMu_maU
# NOTE: Variable names match my implementation for my understanding
def longestConsecutive_optimal_2(nums: List[int]) -> int:    
    elements = set(nums)
    maxLength = 0
    
    # Neetcode looped through nums instead of elements
    for num in elements:
        if (num-1 not in elements):
            length = 0
            while (num + length) in elements:
                length += 1
            maxLength = max(length, maxLength)
    
    return maxLength