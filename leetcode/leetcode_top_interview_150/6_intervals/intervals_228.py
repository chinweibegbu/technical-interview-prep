from typing import List
def summaryRanges(nums: List[int]) -> List[str]:
    # Initialise result to an empty array
    result = []
    # Intialise l and r to the beginning of the array
    l, r = 0, 0

    # For each index and element in the array
    for i, num in enumerate(nums):
        # If we are at the end of the array or the sequence has been broken...
        if (i == len(nums)-1) or (nums[i+1] != num+1):
            # ... And there is exactly one element in the current sequence, add just that element to result
            if (l == r):
                result.append(str(nums[l]))
            # ... And there is more than one element in the current sequence, add both the elements with the joining characters, "->" to result
            else:
                result.append(str(nums[l]) + "->" + str(nums[r]))
            # Then, update l and r to both point to the next element
            l, r = r+1, r+1
        # Else, just increment r
        else:
            r += 1
    
    # Return result
    return result
