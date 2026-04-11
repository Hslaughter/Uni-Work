# Write a program to ask the user to enter four integers and then display the minimum number and the maximum number.
# The program should work exactly as in the following example.

# For example:
# Input 	Result

# 10
# 2
# 15
# 9

	

# Enter the first integer: 10
# Enter the second integer: 2
# Enter the third integer: 15
# Enter the fourth integer: 9

# The minimum number is 2 and the maximum number is 15.

first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
third = int(input("Enter the third integer: ")) 
fourth = int(input("Enter the fourth integer: "))

numbers = [first, second, third, fourth]
min_val = numbers[0]
max_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num


print(f"\nThe minimum number is {min_val} and the maximum number is {max_val}.")