# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
#Programmer = Caiden 
#Date = 10.31.24
#Title = Average
def sum_numbers_from_file():
    total_of_numbers=0

    try:
        with open("numbers.txt","r") as number_file:
            for line in number_file:
                try:
                    total = int(line.strip())
                    total_of_numbers += total


                except ValueError:
                    print("The number is weird")





    except IOError:
        print("the file may not exits")
    print(total_of_numbers)


if __name__ == '__main__':
    sum_numbers_from_file()
