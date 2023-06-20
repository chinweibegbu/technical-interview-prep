def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  if n < 10:
    return n
  not_units, unit = (n//10), (n%10)
  return sum_digits(not_units) + unit

# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)