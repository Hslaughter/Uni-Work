# Study the examples below and write a program that works exactly like the examples using STRING FORMAT.

# For example:
# Input 	Result

# 15

	

# Enter an integer: 15

# You have entered number 15.
# Three numbers after 15 are 16, 17, 18.
# Three numbers before 15 are 14, 13, 12.
# getting user input to use to solve the rest of the problem
number = int(input("Enter an integer: "))
#print statements with a newline to ensure correct formatting
print("\nYou have entered number {}.".format(number))
# string formatting with simple math instead of creating multiple new variables
print("Three numbers after {} are {}, {}, {}.".format(number, number+1, number+2, number+3))
print("Three numbers before {} are {}, {}, {}.".format(number, number-1, number-2, number-3))