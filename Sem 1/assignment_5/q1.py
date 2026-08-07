

# For example:
# Test 	Result

# result = getColorList(intList=[10, 100, 601, 500, 502])
# print(result)

	

# ['purple', 'pink', 'orange', 'pink', 'orange']

# result = getColorList(intList=[102, 101, 100, 99, 499, 500, 501])
# print(result)

	

# ['pink', 'pink', 'pink', 'purple', 'pink', 'pink', 'orange']

# result = getColorList(intList=[])
# print(result)

	

# []
# An integer less than 100 is called a purple number. 
# An integer between 100 and 500 is called a pink number. 
# An integer larger than 500 is called an orange number. 
# Study the examples below and write a function that works exactly like the examples.
def getColorList(intList: list[int]): # create parameters to specify that the list is of type int
    colors = [] # create new empty list to append later
    for i in range(len(intList)): # checking if block
        if intList[i] < 100: 
            colors.append('purple') # append to colors list
        if intList[i] >= 100 and intList[i] <= 500: 
            colors.append('pink')
        if intList[i] > 500:
            colors.append('orange')
    return colors # return list
result = getColorList(intList=[10, 100, 601, 500, 502])
print(result)	

#['purple', 'pink', 'orange', 'pink', 'orange']

result = getColorList(intList=[102, 101, 100, 99, 499, 500, 501])
print(result)

#['pink', 'pink', 'pink', 'purple', 'pink', 'pink', 'orange']

result = getColorList(intList=[])
print(result)

#[]