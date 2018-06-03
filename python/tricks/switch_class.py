#define a value holder class
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True


# function to verify matching case
# => True or False
def case(*args):
    iterator = (arg == switch.value for arg in args)
    return any(iterator)

# Switch example:
for n in range(0,10):
  print(n,":", end="", flush=True)
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
    if True:
        print ("Only single-digit numbers are allowed.")