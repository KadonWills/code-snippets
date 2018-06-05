#define a value holder function
# => True
def switch(value):
    switch.value=value
    return True

#define matching case function
# => True or False
def case(*args):
    return any((arg == switch.value for arg in args))

# Switch example:
print("Describe a number from range:")
for n in range(0,10):
  print(n, end=" ", flush=True)
print()

# Ask for a number and analyze
x=input("n:")
n=int(x)
while switch(n):
    if case(0):
        print ("n is zero;")
        break
    if case(1, 4, 9):
        print ("n is a perfect square;")
        break
    if case(2):
        print ("n is an even number;")
    if case(2, 3, 5, 7):
        print ("n is a prime number;")
        break
    if case(6, 8):
        print ("n is an even number;")
        break
    print ("Only single-digit numbers are allowed.")
