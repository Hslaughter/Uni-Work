# Write a function based on the following specification:
# Function name: 	next_number
# Input arguments: 	1 input argument

#     number: an integer

# Returned values: 	The function returns 1 integer value.

# If the argument number = X is even then the function returns 3X + 1, if X is odd then the function returns 2X + 2.

# For example, if number = 4 then the function returns 13, if number = 5 then the function returns 12.

# For example:
# Test 	Result

# result = next_number(6)
# print(result)

	

# 19

# result = next_number(7)
# print(result)

	

# 16

def next_number(num):
    if num % 2 == 0:
        new = (num*3) + 1
        return new
    else:
        new = (num*2) + 2
        return new

result = next_number(6)
print(result)

result = next_number(7)
print(result)