#fibonacci sequence
def fib(n):
  """Print a Fibonacci series up to n."""
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()

print('Fibonacci Sequence:')  
fib(2000)

print()

#Calculate factorial of n
def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)
  
#Call factorial function and capture result
result = factorial(5)

print('Factorial of 5:')
print(result)
