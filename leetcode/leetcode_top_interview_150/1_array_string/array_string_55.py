from typing import List

def canJump_FAILED(nums: List[int]) -> bool:
    # If there is only one element, return True
    if (len(nums) == 1): return True

    pos, end = 0, len(nums)-1
    
    # For each potential jump value starting from the beginning (index 0)
    for i in range(nums[pos], 0, -1):
        # Jump between 1 and arr[cur] slots
        pos += i
        
        # If we reach or exceed the end, return True
        if (pos >= end):
            return True
        
        # Else...
        else:
            # Continie adding the max of every next slot jumped to...
            # ...until you are no longer moving OR the end is reached/exceeded
            while (pos != end):
                temp = pos
                pos += nums[pos]
                if (temp == pos): 
                    pos -= i
                    break
                if (pos >= end):
                    return True
                
    # If you go through every possible path and do not reach the end, return True
    return False

def canJump_optimal_1(nums: List[int]) -> bool:
    # dp[i] = whether or not we can reach this index
    dp = [False] * len(nums) 
    
    # WHY? We know that we can reach index 0 because that is where we start
    dp[0] = True

    # For each element apart from the first...
    for i in range(1, len(nums)):
        
        # For each element behind the current element, starting from the closest...
        for j in range(i-1,-1,-1):
            
            # ... Check if you have the jump ability at j to cover the dstance between i to j, ensuring that j is reachable
            if (nums[j] >= i - j) and (dp[j]):
                dp[i] = True
                break
    
    # Return the value at the last index
    return dp[-1]
       
# Based on understanding of https://www.youtube.com/watch?v=Yan0cv2cLy8
def canJump_optimal_2(nums: List[int]) -> bool:
    goalpost = len(nums) - 1
    for i in range(len(nums)-2, -1, -1):
        if (i + nums[i] >= goalpost):
            goalpost = i
    return (goalpost == 0)
