from collections import List

def majorityElement_solution(nums: List[int]) -> int:
    # Sort elements
    nums.sort()

    # Return middle element
    # WHY? Because the majotity element occurs more than ⌊n / 2⌋ times...
    # ... i.e. it is at the middle position
    return nums[len(nums)//2]


def majorityElement_optimal(nums: List[int]) -> int:
    # BOYER-MOORE ALGORITHM

    count, candidate = 0, None

    for num in nums:
        # Update the candidate if it the count is 0
        if (count == 0):
            candidate = num
            
        # Increment or decrement count based on if the current element matches the candidate
        count += (1 if (candidate == num) else -1)

    # Return the current candidate
    return candidate
                