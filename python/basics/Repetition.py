# Example of a for loop
words = ['I', 'like', 'to', 'learn', 'python']
for word in words:
     print(len(word), word)

# example of the range function
for i in range(5):
    print(i)

# Break and continue
v = 0
for i in range(1,10):
      if i < 5:
         continue
      if i == 7:
         break
      v = i
print("v = ", v)

# example of using else in a for loop

for i in range(10):
    print('i=',i)
    if i>=3: break
else:
    print('finish i=',i)

# This example demonstrate an infinite loop
v = 0
while True:
    print("forever young")
    v+=1
    if v==100: break
print("I was young forever")