nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
  
# define bubble_sort():
def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1):
      if arr[j] > arr[j+1]:
        swap(arr, j, j+1)
      print("i: {} j: {} >>>> {}".format(i, j, arr))

##### test statements

print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))
