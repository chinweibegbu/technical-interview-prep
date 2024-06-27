from collections import defaultdict
from typing import List

def twoSum_solution(nums: List[int], target: int) -> List[int]:
    # Use a hashmap to store the numbers and their original indices >>> O(n)
    indices = defaultdict(list)
    for i, num in enumerate(nums):
        indices[num].append(i)

    # Get the sorted version of the array >>> O(n log n)
    sorted_nums = sorted(nums)

    # Until we find the solution... >>> O(n)
    # WHY? Because we are assured that there is a solution
    l, r = 0, len(sorted_nums)-1
    while (True):
        # If we have found the solution...
        if (sorted_nums[l] + sorted_nums[r] == target):
            # ... and the two numbers are the same, return the indices at which that number appear
            # WHY? Because we are assured that there is exactly one solution i.e. there must be exactly two numbers which add up to the target
            if (sorted_nums[l] == sorted_nums[r]):
                return indices[sorted_nums[l]]
            # ... and the two numbers are NOT the same, return the indices at which those numbers appear
            else:
                return [indices[sorted_nums[l]][0], indices[sorted_nums[r]][0]]

        # If the current sum is too small, increase the smaller digit
        elif (sorted_nums[l] + sorted_nums[r] < target):
            l += 1
        
        # If the current sum is too big, decrease the larger digit
        else:
            r -= 1

def twoSum_optimal(nums: List[int], target: int) -> List[int]:
    # Create an empty dictionary to hold the elements and their indices as we traverse
    pair_idx = {}

    for i, num in enumerate(nums):
        # If the complement of the current element is in the dictionary, return the current index and the index of said complement
        if (target - num in pair_idx):
            return [i, pair_idx[target - num]]
        
        # Add the current element and its index to the dictionary
        pair_idx[num] = i