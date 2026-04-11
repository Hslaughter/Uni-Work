# Study the examples below and write a program that works exactly like the examples using f-string.
# For example:
# Input 	Result

# Nestle
# 17
# 10

	

# Packaging lollies into boxes
# Please enter the lollies brand: Nestle
# Enter number of lollies: 17
# How many lollies in 1 box? 10

# Nestle lollies packaging calculation
# Number of lollies: 17
# Number of lollies per box: 10
# Number of boxes needed: 1
# Number of lollies left over: 7

# Allens
# 100
# 20

	

# Packaging lollies into boxes
# Please enter the lollies brand: Allens
# Enter number of lollies: 100
# How many lollies in 1 box? 20

# Allens lollies packaging calculation
# Number of lollies: 100
# Number of lollies per box: 20
# Number of boxes needed: 5

#flavour text as per formatting
print("Packaging lollies into boxes")
# collecting user inputs for later computation
brand = input("Please enter the lollies brand: ")
# casting inputs as ints as to be able to do math with them
number = int(input("Enter number of lollies: "))
box = int(input("How many lollies in 1 box? "))
div = number / box
remainder = number % box
# multi-line print statement to keep same formatting
print(f"""\n{brand} lollies packaging calculation
Number of lollies: {number}
Number of lollies per box: {box}
Number of boxes needed: {int(div)} 
Number of lollies left over: {remainder} 
""")

# cast div as int to remove decimal