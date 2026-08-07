# Write a program to display the following exact output using while-loop statement.
# 1; 3; 5; 7; 9.
i = 1
while i <= 9:
    if i < 9:
        print(f"{i}; ", end='')
        
    else:
        print(f"{i}.", end='')
    i += 2      