from typing import List

def longestCommonPrefix_initial(strs: List[str]) -> str:
    index = 0
    prefix = ""

    # Edge case #1: Any empty words
    empty = [x for x in strs if len(x) == 0]
    if (len(empty) > 0):
        return prefix

    # Edge case #2: Only one word
    if (len(strs) == 1):
        return strs[0]

    while True: 
        # If the first word has any characters left, get the next one under consideration + Else, return what we already have
        if (index < len(strs[0])):
            cur = strs[0][index]
        else:
            return prefix

        # For each word, continue if the character under consideration exists and is the same + Else, return, what we already have
        for s in strs:
            if ((index >= len(s)) or (s[index] != cur)):
                return prefix

        # Update the prefix and current index
        prefix += strs[0][index]
        index += 1

def longestCommonPrefix_solution(strs: List[str]) -> str:
    index = 0
    prefix = ""

    while True: 
        for i in range(len(strs)):

            # If we are back to the beginning of the words array, update cur
            if ((i == 0) and (index < len(strs[i]))):
                cur = strs[i][index]

            # If the index has passed the length of any of the strings OR the character at index does not match cur, return what we have
            if ((index >= len(strs[i])) or (strs[i][index] != cur)):
                return prefix

        # Update the prefix and current index
        prefix += cur
        index += 1
        
# Based on code sample at a higher percentile than my Solution Approach
# Modified variables for my understanding and better visibility
def longestCommonPrefix_optimal(strs: List[str]) -> str:
    prefix = ""
    first = strs[0]

    for i in range(len(first)):
        for s in strs:
            if i == len(s) or s[i] != first[i]:
                return prefix
        prefix += first[i]
    
    return prefix