# Write a program to generate a list of square numbers.
#  The program should work exactly like the following example.

# For example:
# Input 	Result

# 7

	

# How many square numbers to generate? 7
# Here is a list of generated squares: [0, 1, 4, 9, 16, 25, 36]


amnt = int(input("How many square numbers to generate? "))

squarelist = []
for i in range(amnt):
    squarelist.append(i*i)

print("Here is a list of generated squares: ",squarelist)