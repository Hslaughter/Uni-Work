# Write a program to display the following exact output using while-loop statement and string format.

# For example:
# Result

#  2 +  2 =  4
#  4 +  4 =  8
#  6 +  6 = 12
#  8 +  8 = 16
# 10 + 10 = 20

i = 0
while (i < 10):
    i += 2
    print(f"{i:>2} + {i:>2} = {i+i:>2}")