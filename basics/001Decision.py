# ------------------------------------------
# program example for decision statement
# article link: https://sagecode.net/python-decision/
# ------------------------------------------
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
pass

# end program