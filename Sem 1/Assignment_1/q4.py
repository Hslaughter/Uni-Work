# Enter 1st positive integer: 37
# Enter 2nd positive integer: 10

# --Math operations--
# Add: 37 + 10 = 47
# Minus: 37 - 10 = 27
# Times: 37 * 10 = 370
# Modulo: 37 % 10 = 7
# Division: 37 / 10 = 3.7
# Floor division: 37 // 10 = 3

# creating inputs and assigning them to variables
first = int(input("Enter 1st positive integer: "))
second = int(input("Enter 2nd positive integer: "))

# print statements with formatting as provided
print("\n--Math operations--")
print(f"Add: {first} + {second} = {first + second}")
print(f"Minus: {first} - {second} = {first - second}")
print(f"Times: {first} * {second} = {first * second}")
print(f"Modulo: {first} % {second} = {first % second}")
print(f"Division: {first} / {second} = {first / second}")
print(f"Floor division: {first} // {second} = {first // second}")
# doing computations within the f string as to not have to make additional variables