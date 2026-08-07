# result = even_number_string(startNumber=5, endNumber=10, separator="$")
# print(result)

	

# 6$8$10

# result = even_number_string(startNumber=4, endNumber=13, separator="a")
# print(result)

	

# 4a6a8a10a12

# result = even_number_string(startNumber=51, endNumber=53, separator="b")
# print(result)

	

# 52

def even_number_string(startNumber, endNumber, separator):
    result = "" # initialise empty string that we will later append to return
    while startNumber <= endNumber: # set while loop conditions to establish our "Range"
        if startNumber % 2 == 0: # check if number is even
            if result != "": # on first loop, separator will not get added. every other loop its added first to avoid a trailing letter
                result += f"{separator}" # append separator to result
            result += f"{startNumber}" # append start number to result
        startNumber += 1 # increment outside of if statement, so even if its odd it increments
    return result

result = even_number_string(startNumber=5, endNumber=10, separator="$")
print(result)
result = even_number_string(startNumber=4, endNumber=13, separator="a")
print(result)
result = even_number_string(startNumber=51, endNumber=53, separator="b")
print(result)