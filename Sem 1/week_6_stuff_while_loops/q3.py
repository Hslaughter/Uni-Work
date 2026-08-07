# Input 	Result

# 5
# 10
# -1
# 3
# 0
# -5
# q

	

# Enter an integer or q to quit: 5
# Enter an integer or q to quit: 10
# Enter an integer or q to quit: -1
# Enter an integer or q to quit: 3
# Enter an integer or q to quit: 0
# Enter an integer or q to quit: -5
# Enter an integer or q to quit: q

# Summary information:
# You have entered 6 integers.
# The sum of these numbers is 12.
# There are 2 even numbers.
# There are 4 odd numbers.
# There are 3 positive numbers.
# There are 2 negative numbers.
answer = ""
count = 0
even = 0
odd = 0
negative = 0
sumAll = 0
positive = 0
while answer != "Q":
    answer = input("Enter an integer or q to quit: ").upper()
    if answer == "Q":
        break
    count += 1
    answer = int(answer)
    sumAll += answer
    if answer < 0:
        negative += 1
    if answer > 0:
        positive += 1
    if answer % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"""
Summary information:
You have entered {count} integers.
The sum of these numbers is {sumAll}.
There are {even} even numbers.
There are {odd} odd numbers.
There are {positive} positive numbers.
There are {negative} negative numbers.""")