from typing import List

def maxAreaheight_initial(height: List[int]) -> int:
    l, r = 0, len(height)-1
    maximum = 0
    while l < r:
        maximum = max(maximum, min(height[l], height[r]) * (r - l))
        if (height[l-1] <= height[r+1]):
            l += 1
        else:
            r -= 1
    return maximum

# Based on understanding of https://youtu.be/UuiTKBwPgAo
def maxAreaheight_optimal(height: List[int]) -> int:
    l, r = 0, len(height)-1
    maximum = 0
    while l < r:
        maximum = max(maximum, min(height[l], height[r]) * (r - l))
        if (height[l] <= height[r]):
            l += 1
        else:
            r -= 1
    return maximum
