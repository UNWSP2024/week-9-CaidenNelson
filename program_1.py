# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.
#Programmer = caiden
#Date = 10.28.24
#Title = Number of Names
def count_file_lines():
    ######################
    # Add your code here #
    ######################
    names = open("names.txt","r").read()
    new_names = names.split()
    new_names = len(new_names)
    print(f'there are {new_names} names in the file names.txt')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
