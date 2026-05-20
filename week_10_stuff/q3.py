# Write a program to repeatedly ask the user to enter an integer number, until the user enters QUIT.
# Then display the list of all the entered numbers.
# The program should work exactly like the following example.

# For example:
# Input 	Result

# 10
# 5
# 1
# 2
# QUIT

	

# Enter an integer (enter QUIT to quit): 10
# Enter an integer (enter QUIT to quit): 5
# Enter an integer (enter QUIT to quit): 1
# Enter an integer (enter QUIT to quit): 2
# Enter an integer (enter QUIT to quit): QUIT
# You have entered: 10, 5, 1, 2.
inplist = []
quitcheck = True
while quitcheck:
    answer = input("Enter an integer (enter QUIT to quit): ")
    if answer.upper() == "QUIT":
        quitcheck = False
        print("You have entered:", end=" ")
        print(*inplist, sep=", ", end=".")
        break
    answer = int(answer)
    inplist.append(answer)