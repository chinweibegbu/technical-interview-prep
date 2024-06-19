from typing import List

def twoSum_initial(numbers: List[int], target: int) -> List[int]:
    # Edge case: There are two numbers
    if (len(numbers) == 2):
        return [1,2]

    l, r = 0, 1
    while l < len(numbers):
        if ((numbers[l] + numbers[r]) == target):
            break
        elif ((numbers[l] + numbers[r]) < target):
            l += 1
            r += 1
        elif ((numbers[l] + numbers[r]) > target):
            l -= 1
    
    return [l+1, r+1]

def twoSum_solution(numbers: List[int], target: int) -> List[int]:
    l, r = 0, 1
    while l < len(numbers):
        if ((numbers[l] + numbers[r]) == target):
            break
        elif ((numbers[l] + numbers[r]) < target):
            l += 1
            r += 1
        elif ((numbers[l] + numbers[r]) > target):
            l -= 1
    
    return [l+1, r+1]

def twoSum_optimal(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers)-1
    while l < len(numbers):
        if ((numbers[l] + numbers[r]) == target):
            break
        elif ((numbers[l] + numbers[r]) < target):
            l += 1
        elif ((numbers[l] + numbers[r]) > target):
            r -= 1
    
    return [l+1, r+1]