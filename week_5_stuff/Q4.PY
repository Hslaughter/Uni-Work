# Write a program to display the following exact output using for-loop statement.
# 2, 4, 6, 8, 10.

for i in range(1,11):
    result = i * 2
    if result < 10:
        print(f"{result}, ", end="")
    else:
        print(f"{result}.",end="")
        break