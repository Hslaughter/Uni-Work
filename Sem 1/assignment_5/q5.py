# Study the examples below and write a program that works exactly like the examples.

# For example:
# Input 	Result

# MATH111
# 5
# CS102
# 4
# BUS304
# 7
# Q

	

# Enter subject code (Q to quit): MATH111
# Enter credit point: 5
# Enter subject code (Q to quit): CS102
# Enter credit point: 4
# Enter subject code (Q to quit): BUS304
# Enter credit point: 7
# Enter subject code (Q to quit): Q
# Subject you have entered:
# MATH111: 5 cp
# CS102: 4 cp
# BUS304: 7 cp

# Q

	

# Enter subject code (Q to quit): Q
# Subject you have entered:

quitcheck = True # create loop variable
subject = {} # create empty dict
while quitcheck: # create while loop
    code = input("Enter subject code (Q to quit): ").upper() # input for code
    if code == 'Q': # check to see if the loop needs to be broken
        quitcheck = False # break loop
        break
    credit = input("Enter credit point: ") # input for credit point
    subject[code] = credit # append dict
print("Subject you have entered:") # print
for code, credit in subject.items(): # loop through dict
    print(f"{code}: {credit} cp") # print each item