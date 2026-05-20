# Hi! I am Sam

	

# Enter a sentence: Hi! I am Sam
# String list: ['0H0', '1i1', '2!2', '3 3', '4I4', '5 5', '6a6', '7m7', '8 8', '9S9', '10a10', '11m11']

# wollongong

	

# Enter a sentence: wollongong
# String list: ['0w0', '1o1', '2l2', '3l3', '4o4', '5n5', '6g6', '7o7', '8n8', '9g9']


sentence = input("Enter a sentence: ") # create input variable
stringlist = [] # create empty list to append to

for i in range(len(sentence)): # create loop for the length of the input
    stringlist.append(f"{i}{sentence[i]}{i}") # append to list with correct formatting

print("String list:",stringlist) # print statement and list