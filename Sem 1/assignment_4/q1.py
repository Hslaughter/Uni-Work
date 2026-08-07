# print_equation(startNumber=2, endNumber=5)

	

# 2 + 3 + 2 x 3 = 11
# 3 + 4 + 3 x 4 = 19
# 4 + 5 + 4 x 5 = 29
# 5 + 6 + 5 x 6 = 41

# print_equation(startNumber=10, endNumber=13)

	

# 10 + 11 + 10 x 11 = 131
# 11 + 12 + 11 x 12 = 155
# 12 + 13 + 12 x 13 = 181
# 13 + 14 + 13 x 14 = 209

# print_equation(startNumber=7, endNumber=7)

	

# 7 + 8 + 7 x 8 = 71

def print_equation(startNumber, endNumber):
    while startNumber <= endNumber: # set loop to only finish when start is <= end
        increment = startNumber + 1 # create variable to make fstring more legible
        product = startNumber + increment + startNumber * increment # create variable for similar purpose as increment
        print(f"{startNumber} + {increment} + {startNumber} x {increment} = {product} ") # use fstring to display result
        startNumber += 1 # increment start_number by 1
 



print_equation(startNumber=10, endNumber=13)
