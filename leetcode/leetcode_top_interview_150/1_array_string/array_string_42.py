from typing import List

# Based on understanding from https://www.youtube.com/watch?v=ZI2z5pq0TqA
def trap_optimal(height: List[int]) -> int:
    maxLefts, maxRights = [None]*len(height), [None]*len(height)
    maxLeft, maxRight = 0, 0
    trapped = []
    for i in range(len(height)):
        maxLefts[i] = maxLeft
        if (height[i]) > maxLeft:
            maxLeft = height[i]
    for i in range(len(height)-1, -1, -1):
        maxRights[i] = maxRight
        if (height[i]) > maxRight:
            maxRight = height[i]
    for i in range(len(height)):
        trapped.append(max(0, min(maxLefts[i], maxRights[i]) - height[i]))
    return sum(trapped)
    