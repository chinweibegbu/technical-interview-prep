from typing import List

def minSubArrayLen_initial_1_FAILED(target: int, nums: List[int]) -> int:
    for window in range(1, len(nums)+1):
        for i in range(0, len(nums)):
            if ((i + window < len(nums)+1) and (sum(nums[i:i+window]) >= target)):
                return window
    
    return 0

def minSubArrayLen_initial_2_FAILED(target: int, nums: List[int]) -> int:
    l, r = 0, 0
    minimum = len(nums) + 1
    while (l <= r) and (r < len(nums)):
        if (sum(nums[l:r+1]) < target):
            r += 1
        else:
            minimum = min(minimum, (r-l+1))
            l += 1
        
    return minimum if minimum < len(nums)+1 else 0

def minSubArrayLen_optimal(target: int, nums: List[int]) -> int:
    l, r = 0, 0
    minimum = len(nums) + 1
    total = nums[0]
    while (l <= r) and (r < len(nums)):
        if (total < target):
            r += 1
            total += nums[r] if r < len(nums) else 0
        else:
            minimum = min(minimum, (r-l+1))
            total -= nums[l]
            l += 1
        
    return minimum if minimum < len(nums)+1 else 0