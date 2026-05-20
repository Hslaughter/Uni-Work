# Study the examples below and write a function that works exactly like the examples.

# For example:
# Test 	Result

# displayEquation(numberList=[7, 33, 6, -5])

	

# Index 0: equation 7 x 10 = 70
# Index 1: equation 33 x 10 = 330
# Index 2: equation 6 x 10 = 60
# Index 3: equation -5 x 10 = -50

# displayEquation(numberList=[15, 28, 4, 0, 1])

	

# Index 0: equation 15 x 10 = 150
# Index 1: equation 28 x 10 = 280
# Index 2: equation 4 x 10 = 40
# Index 3: equation 0 x 10 = 0
# Index 4: equation 1 x 10 = 10

def displayEquation(numberList: list[int]): # create method name and set parameters with list type of int
    for i in range(len(numberList)): # create loop to loop as long as the list is
        print(f"Index {i}: equation {numberList[i]} x 10 = {numberList[i]*10}") # print equation

displayEquation(numberList=[7, 33, 6, -5])
print()
displayEquation(numberList=[15, 28, 4, 0, 1])