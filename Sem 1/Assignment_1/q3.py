# Study the examples below and write a program that works exactly like the examples using STRING FORMAT. All money calculations are in whole dollars.
# For example:
# Input 	Result

# Dell
# 100
# 30
# 2

# --Laptop rental calculation--
# Enter the laptop brand: Dell
# Enter the application cost: 100
# Enter the monthly cost: 30
# Enter the number of months: 2

# Rental cost for Dell laptop
# Application cost: $100
# Rental cost: $30 x 2 month = $60
# Total cost: $100 + $60 = $160

# Froggy
# 0
# 10
# 5

	

# --Laptop rental calculation--
# Enter the laptop brand: Froggy
# Enter the application cost: 0
# Enter the monthly cost: 10
# Enter the number of months: 5

# Rental cost for Froggy laptop
# Application cost: $0
# Rental cost: $10 x 5 month = $50
# Total cost: $0 + $50 = $50

#opening title statement
print("--Laptop rental calculation--")
# getting inputs from user and assigning them to variables
brand = input("Enter the laptop brand: ")
# casting variables as intergers for computation
appCost = int(input("Enter the application cost: "))
monthCost = int(input("Enter the monthly cost: "))
monthNo = int(input("Enter the number of months: "))
# final print statements in line with the provided formatting
print("\nRental cost for {} laptop".format(brand)) # new line statement for spacing
print("Application cost: ${}".format(appCost))
print("Rental cost: ${} x {} month = ${}".format(monthCost, monthNo, monthCost*monthNo)) # doing computation within formatting
print("Total cost: ${} + ${} = ${}".format(appCost, monthCost*monthNo, appCost + (monthCost*monthNo)))