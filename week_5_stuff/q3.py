# Write a program to display the following exact output using for-loop statement.
# 1 : 2 : 3 : 4 : 5 : 6 : 7 : 8 : 9 : 10

for i in range(1,11):
    print(f"""{i}""",end="")
    if i < 10:
        print(" : ",end="")
    else:
        
        break