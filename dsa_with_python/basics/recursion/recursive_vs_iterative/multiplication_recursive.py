def multiplication(num_1, num_2):
  # Edge case: Multiplication by 0
  if (num_1 == 0 or num_2 == 0): return 0

  # Edge case: Multiplication by 1
  if num_1 == 1: return num_2
  if num_2 == 1: return num_1

  # Base case
  if num_2 == 1:
    return num_1
  # Recursive step
  return multiplication(num_1, num_2-1) + num_1

# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)
