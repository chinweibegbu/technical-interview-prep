from typing import List

def removeDuplicates(nums: List[int]) -> int:
    # Egde case: Less than two elements
    if (len(nums) < 2): return len(nums)

    # Initialise pointers to represent last unique element and a parser
    # NOTE: We know that the first element of the array is unique, hence the 0
    u, p = 0, 1
    
    # Continue until you exceed the length of the list
    while (p < len(nums)):
        # If you reach a new unique element, swap it with the element IN FRONT of the last unique element
        if (nums[u] != nums[p]):
            nums[u+1], nums[p] = nums[p], nums[u+1]
            
            # Increment the unique counter to account for the new unique element
            u += 1
            
        # Continue to the next element in the array
        p += 1
    
    # Return the number of unique elements (NOTE: u is an index)
    return u+1
    