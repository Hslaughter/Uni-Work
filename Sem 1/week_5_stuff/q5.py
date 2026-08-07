# Write a program to display the following exact output using for-loop statement.
# 1; 3; 5; 7; 9.

for i in range(1,10,2):
    
    if i < 9:
        print(f"{i}; ", end="")
        
    else:
        print(f"{i}.",end="")
        break