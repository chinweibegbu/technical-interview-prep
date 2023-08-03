from typing import List

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Edge case: Second list is empty
    if (n == 0):
        pass
    # Edge case: Lists are the same length (ie. first list is empty)
    elif (m == 0):
        for i in range(len(nums2)):
            nums1[i] = nums2[i]
    # Regular case: Both lists have content
    else:
        nums = nums1[:(len(nums1)-n)]
        c, x, y = 0, 0, 0
        while (c < len(nums1)):
            if (x >= len(nums)):
                nums1[c] = nums2[y]
                y += 1
            elif (y >= len(nums2)):
                nums1[c] = nums[x]
                x += 1
            elif ((x < len(nums)) and (nums[x] <= nums2[y])):
                nums1[c] = nums[x]
                x += 1
            elif ((y < len(nums2)) and (nums[x] > nums2[y])):
                nums1[c] = nums2[y]
                y += 1
            c += 1
    return None

# Optimal Solution Code (by KeshariNilesh13)
# Source: https://leetcode.com/problems/merge-sorted-array/solutions/3432899/simple-python-solution-with-3-pointers/)
def merge_optimal(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Start from the ends of the lists
    i,j,k = m-1,n-1,m+n-1
    # While the second list has content
    while j>=0:
        # If the first list has content and the first list's element is greater than the second list's...
        if i>=0 and nums1[i]>nums2[j]:
            # Add that element of the first list
            nums1[k]=nums1[i]
            i-=1
        # If the first list has no content OR the first list's element is less than the second list's...
        else:
            # Add that element of the second list
            nums1[k]=nums2[j]                
            j-=1
        k-=1