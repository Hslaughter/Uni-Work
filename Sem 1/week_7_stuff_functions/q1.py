# Write a function based on the following specification:
# Function name: 	triple
# Input arguments: 	1 input argument

#     sentence: a string

# Returned values: 	The function returns 1 string value.

# The function returns a new string constructed from sentence where each character gets repeated 3 times.

# For example, if sentence is Uni then the function returns the string UUUnnniii 

def triple(word):
    new = ""
    for i in range(len(word)):
        letter = word[i]
        for j in range(3):
            new = new + letter
    return new
result = triple("Hi")
print(result)