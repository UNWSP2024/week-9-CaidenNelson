# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
#Programmer = Caiden 
#Date = 10.28.24
#title = Random number storage
import random

total_numbers = int(input('how many random numbers would you like to write into the file? It can hold up to 1000 numbers that can each be anywhere between 1 and 500 '))

file = open("Random.txt","w")


for i in range(total_numbers):
    number = random.randint(1, 500)
    file.write(str(f'{number}\n'))

file.close()

file = open("Random.txt","r")
line = file.read()
print(line)
