#Author: Claudiu Moise
#Hello world comparison between Java and Python
#One with a static message and one where the input is user defined

#Allows us to use the readline method
#No need to name program
import sys

print("Hello, World!")

print('Please enter a welcome message')
greeting = sys.stdin.readline()
print('Your new greeting is:', greeting)
