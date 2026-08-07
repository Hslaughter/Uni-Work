# Input 	Result

# 52123

	

# Enter an integer: 52123
# A beautiful number ends with 123
# This number is beautiful
# This number is odd
# This number is positive

# 44446

	

# Enter an integer: 44446
# A beautiful number ends with 123
# This number is NOT beautiful
# This number is even
# This number is positive

    

    
number = int(input("Enter an integer: "))
print("A beautiful number ends with 123")
x = abs(number)
lastnums = x % 1000
if lastnums == 123:
    print(f"""This number is beautiful
This number is odd""")
    if number >= 0:
        print("This number is positive")
    else:
        print("This number is negative")

else:
    print("This number is NOT beautiful")
    if x % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

    if number == 0:
            print("This number is zero")
    if number > 0:
        print("This number is positive")
        
    elif number < 0:
        print("This number is negative")
        

