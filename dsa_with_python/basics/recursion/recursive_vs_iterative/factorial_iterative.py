def factorial(n):
  result = 1
  for item in range(2, n+1):
    result *= item
  return result

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)