from collections import List

def rotate_initial(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    temp = [None]*n

    # Use modulus to get the minimum number of moves to get the expected array
    # e.g. k=3 and k=10 mean the same thing to an array of length 7
    k = k%n

    # Edge case: k is 0 pr a multiple of n (i.e. no need to rotate)
    if (k == 0): return

    # Copy the array in rotated order to a temporary array
    cur = n-k
    for i in range(n):
        temp[i] = nums[(cur%n)]
        cur += 1
    
    # Copy the element back into the original array
    for i in range(n):
        nums[i] = temp[i]

# Solution source: https://leetcode.com/problems/rotate-array/solutions/5189694/easy-python-solution
def rotate_optimal(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n  # In case k is larger than n
    
    # Helper function to reverse a portion of the array
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Reverse the entire array
    reverse(0, n - 1)
    # Reverse the first k elements
    reverse(0, k - 1)
    # Reverse the remaining n - k elements
    reverse(k, n - 1)
