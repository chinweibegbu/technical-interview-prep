def fibonacci(n):
  sequence = [0,1]
  if (n==0 or n==1):
    return sequence[n]
  for i in range(2, n+1):
    sequence.append(sequence[i-1] + sequence[i-2])
  return sequence[n]  

# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)