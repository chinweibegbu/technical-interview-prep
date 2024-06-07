from typing import List

def merge_solution(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    # Initialise pointers to the back of nums1 elements, nums2 and nums1
    i, j, k = m-1, n-1, (m+n)-1
    
    # While there are elements in both nums1 and nums2...
    # ...Add the larger element of the two current pointers (i, j) to the current front of the merged list (k)
    while ((i >= 0) and (j >= 0)):
        if (nums1[i] >= nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
        
    # If there is anything left in nums2, add it to the beginning of nums1
    if (j > i):
        for x in range(j+1):
            nums1[x] = nums2[x]
