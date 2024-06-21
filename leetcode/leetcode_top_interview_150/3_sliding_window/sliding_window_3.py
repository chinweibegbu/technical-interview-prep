def lengthOfLongestSubstring_solution(s: str) -> int:
    # 1. Initialise both pointers to 0 (to account for the 0-length string edge case)
    l, r = 0, 0
    
    # 2. Initialise maximum to 0 (to account for the 0-length string edge case)
    maximum = 0 
    
    # 3. Initialise an empty dictionary to track all characters in the current substring
    tracker = {} 
    
    # 4. While the window has not exceeded the length of the string
    while (r < len(s)):
        # 5a. If the traverser, r, is already in the substring
        if (s[r] in tracker):
            # 5b. Update the maximum to the larger of its current value and the window length
            # WHY r-l INSTEAD OF r-l+1? Because r is pointing at a repeating character, which should NOT be counted
            maximum = max(maximum, (r - l))
            
            # 5c. Update the beginning pointer to the character immediately the first occurence of the repeated character
            while True:
                # Delete the current character from tracker and shift the beginning pointer by 1
                del tracker[s[l]]
                l += 1
                
                # If the character before updating was the repeated character, we have finished updating, so break 
                if s[l-1] == s[r]:
                    break
        # 6. Else, add the current character to tracker and increment the window by 1 
        else:
            tracker[s[r]] = 1
            r += 1
            
    # 7. Update the maximum one more time
    # WHY? To account for the second reason to update the maximum, which is when we've reached the end
    maximum = max(maximum, (r - l))
    
    # 8. Return the maximum
    return maximum