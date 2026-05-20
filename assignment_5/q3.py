# Study the examples below and write a function that works exactly like the examples.

# For example:
# Test 	Result

# add2Number(numberList=[7, 33, 6, 3, 10])

	

# Equation here:
# 7 + 33 = 40
# 33 + 6 = 39
# 6 + 3 = 9
# 3 + 10 = 13

# add2Number(numberList=[1, 5])

	

# Equation here:
# 1 + 5 = 6

# add2Number(numberList=[7])

	

# Equation here:

# add2Number(numberList=[])

	

# Equation here:

def add2Number(numberList: list[int]): # create method signature with correct typing of list
    print("Equation here:")
    for i in range(len(numberList) -1): # make sure i+1 does not go out of range 
        print(f"{numberList[i]} + {numberList[i+1]} = {numberList[i]+numberList[i+1]}") # perform calculation in fstring

add2Number(numberList=[7, 33, 6, 3, 10])       
add2Number(numberList=[1, 5])
add2Number(numberList=[7])
add2Number(numberList=[])
    