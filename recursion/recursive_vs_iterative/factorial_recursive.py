def factorial(n):  
  if n < 0:    
    return ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)

# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)