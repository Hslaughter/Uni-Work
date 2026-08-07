# Write a program to generate a list of Fibonacci numbers.
# The program should work exactly like the following example.

# For example:
# Input 	Result

# 6

	

# How many Fibonacci numbers to generate? 6
# Here is a list of generated Fibonacci numbers: [0, 1, 1, 2, 3, 5]

fib = []
n = int(input("How many Fibonacci numbers to generate? "))
for i in range(n):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i-1]+fib[i-2])
print("Here is a list of generated Fibonacci numbers:",fib)