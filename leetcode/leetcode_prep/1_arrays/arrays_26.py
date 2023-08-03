from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    # Set current to the first element and traverser to its immediate neighbour
    current = 0
    traverser = 1

    # Stop when the whole list has been traversed
    while traverser < len(nums):
        # If the traverser is pointing to an element equal to the current, skip element
        if (nums[current] == nums[traverser]):
            # Move traverser forward by 1
            traverser += 1
            continue
        # If traverser is pointing to a different element (i.e. we know it is unique as the list is ordered)...
        else:
            # Swap what is in front of current with the element traverser is pointed at
            nums[current+1], nums[traverser] = nums[traverser], nums[current+1]

            # Move both current and traverser by 1 such that current is pointing at the new largest unique element
            # and traverser is continuing its traversal throughout nums
            current += 1
            traverser += 1

    # Seeing as current holds the index of the largest unique element, return current+1 to account for zero-indexing
    return current+1
