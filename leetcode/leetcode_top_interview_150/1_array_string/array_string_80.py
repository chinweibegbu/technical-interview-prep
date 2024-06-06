from collections import List

def removeDuplicates_initial(nums: List[int]) -> int:
    # Egde case: Less than two elements
    if (len(nums) < 2): return len(nums)

    # Initialise pointers for the last unique element, a parser and a counter to track how many times an element has occured
    u, p, c = 0, 1, 1
    
    # Continue until the parser pointer exceeds the limit of the array
    while (p < len(nums)):
        
        # If the last unique element and current element are the same and it hasn't occured up to twice...
        if ((nums[u] == nums[p]) and (c < 2)):
            
            # ... AND If the unique element is not beside its next occurence...
            # ... ... Swap the element in front of last unique element and current then update unique pointer
            if (abs(u-p) != 1):
                nums[u+1], nums[p] = nums[p], nums[u+1]
                
            # ... Update unique pointer to point to the new instance of the same unique element
            # ... Then increment the counter to account for the new instance
            u += 1
            c += 1
            
        # If the last unique element and current element are NOT the same...
        # ... Swap the element in front of last unique element and current then update unique pointer
        # ... Then reset the counter to 1
        elif (nums[u] != nums[p]):
            nums[u+1], nums[p] = nums[p], nums[u+1]
            u += 1
            c = 1
            
        # Under any circumstance, update the parser pointer
        p += 1
    
    # Return the number of unique elements (NOTE: u is an index)
    return u+1

def removeDuplicates_solution(nums: List[int]) -> int:
    # Egde case: Less than two elements
    if (len(nums) < 2): return len(nums)

    # Initialise pointers for the last unique element, a parser and a counter to track how many times an element has occured
    u, p, c = 0, 1, 1
    
    # Continue until the parser pointer exceeds the limit of the array
    while (p < len(nums)):
        
        # If the last unique element and current element are the same and it hasn't occured up to twice...
        if ((nums[u] == nums[p]) and (c < 2)):
            
            # ... AND If the unique element is not beside its next occurence...
            # ... ... Swap the element in front of last unique element and current then update unique pointer
            if (abs(u-p) != 1):
                nums[u+1], nums[p] = nums[p], nums[u+1]
                
            # ... Update unique pointer to point to the new instance of the same unique element
            # ... Then increment the counter to account for the new instance
            u += 1
            c += 1
            
        # If the last unique element and current element are NOT the same...
        # ... Replace the element in front of last unique element with the current then update unique pointer
        # ... Then reset the counter to 1
        elif (nums[u] != nums[p]):
            nums[u+1] = nums[p]
            u += 1
            c = 1
            
        # Under any circumstance, update the parser pointer
        p += 1
    
    # Return the number of unique elements (NOTE: u is an index)
    return u+1

def removeDuplicates_optimal(nums: List[int]) -> int:
    # Egde case: Less than THREE elements
    if (len(nums) < 3): return len(nums)
    
    # Initialise unique_length to 1 because we are certain the first element is unique
    unique_length = 1
    # Initialise cur_frequency to 1 because we only have one element so far
    cur_frequency = 1
    
    for i in range(1, len(nums)):
        # If cur and its prev are not the same, increase its frequency
        if (nums[i] == nums[1-1]):
            cur_frequency += 1
        # Else, reset it to 1
        else:
            cur_frequency = 1

        # If cur has not exceeded the limit of 2, move it to where the end of the modified subarray
        if (cur_frequency <= 2):
            nums[unique_length] = nums[i]
            unique_length += 1
        
    # Return the length of the modified subarray
    return unique_length