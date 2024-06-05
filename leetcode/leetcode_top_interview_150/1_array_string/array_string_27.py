from collections import List

def removeElement_initial(nums: List[int], val: int) -> int:

    # Edge case #1: Empty list
    if (len(nums) == 0):
        return 0

    # Return the position in the array, starting from the current back, that is NOT val
    def update_back(b):
        while (b >= 0):
            # If current back is val and there is nowhere to go, all elements are val
            if ((nums[b] == val) and (b-1 < 0)):
                return 0
            # If current back is val and there is somewhere to go, decrement back
            elif ((nums[b] == val) and (b-1 >= 0)):
                b -= 1
            # If current back is NOT val, stop iterating
            else:
                break
        # Return the updated back pointer
        return b

    # Initialise the front and back pointers to the beginning of the array and a valid back (i.e. NOT val)
    f, b = 0, update_back(len(nums)-1)

    # Edge case #2: All elements are val (applies to [2, 2, 2] and [2] where val is 2)
    if ((b == 0) and (nums[b] == val)):
        return 0
    
    while (f < b):       
        # Swap or continue based on if cur is val or not, respectively
        if (nums[f] == val):
            nums[f], nums[b] = nums[b], nums[f]
            b = update_back(b)
        else:
            f += 1

    # Return the number of elements in the array (index of valid elements + 1)
    return (f+1)
