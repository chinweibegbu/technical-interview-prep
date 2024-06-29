from typing import List
def first_element(a):
    return a[0]

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sort intervals by their first element
    intervals.sort(key=first_element)

    # Initialise an empty array to store distinct intervals
    distinct = []
    # Initialise start and end to point to the first interval
    start, end = 0, 0
    
    # Parse out distinct intervals >>> O(n)
    while end < len(intervals):
        # If we've reached the end OR current's end does NOT exceeds next's start, add the current start and end to distinct >>> O(1)
        if (end == len(intervals)-1) or (intervals[end][1] < intervals[end+1][0]):
            distinct.append([intervals[start][0], intervals[end][1]])
            start, end = end+1, end+1
        
        # If current's end exceeds both next's start and end, delete next >>> O(n)
        # WHY? Because its interval is already captured by current
        elif (intervals[end][1] >= intervals[end+1][0]) and (intervals[end][1] >= intervals[end+1][1]):
            del intervals[end+1]
        
        # If current's end exceeds next's start but NOT end, increment current >>> O(1)
        elif (intervals[end][1] >= intervals[end+1][0]) and not (intervals[end][1] >= intervals[end+1][1]):
            end += 1
    
    # Return distinct intervals
    return distinct