from typing import List

def productExceptSelf_initial_FAILED(nums: List[int]) -> List[int]:
    answer = []
    cur = 1
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (j == i):
                continue
            if (nums[j] == 0):
                cur = 0
                break
            cur *= nums[j]
        answer.append(cur)
        cur = 1
    return answer


def productExceptSelf_solution_1(nums: List[int]) -> List[int]:
    prefixes = {}
    suffixes = {}
    n = len(nums)

    # Pre-calculate all prefixes (NOT including last element)
    for i in range(n-1):
        if (i == 0):
            prefixes[i] = nums[i]
        else:
            prefixes[i] = prefixes[i-1] * nums[i]

    # Pre-calculate all suffixes (NOT including first element)
    for j in range(n-1, 0, -1):
        if (j == n-1):
            suffixes[j] = nums[j]
        else:
            suffixes[j] = nums[j] * suffixes[j+1]        

    # Calculate all answers
    answers = [None]*n
    for i in range(n):
        answers[i] = (prefixes[i-1] if i>0 else 1) * (suffixes[i+1] if i<(n-1) else 1)

    return answers 

def productExceptSelf_solution_2(nums: List[int]) -> List[int]:
    prefixes = {}
    suffixes = {}
    n = len(nums)

    # Pre-calculate all prefixes and suffixes
    # Do NOT calculate based on a cache memory first element in prefixes and last element in suffixes
    for i in range(n-1):
        if (i == 0):
            prefixes[i] = nums[i]
            suffixes[n-1-i] = nums[n-1-i]
        else:
            prefixes[i] = prefixes[i-1] * nums[i]
            suffixes[n-1-i] = suffixes[(n-1-i)+1] * nums[n-1-i] 

    # Calculate answers based on pre-calculated answers
    answers = [None]*n
    for i in range(n):
        answers[i] = (prefixes[i-1] if i>0 else 1) * (suffixes[i+1] if i<(n-1) else 1)

    return answers 

