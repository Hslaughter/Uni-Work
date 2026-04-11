# Input 	Result

# 20
# 4
# 5

	

# Enter the bound to stop: 20
# Enter initial number: 4
# Increased by: 5

# Here is the display:
# 4 + 5 = 9
# Checking bound: 9 <= 20 continue
# 9 + 5 = 14
# Checking bound: 14 <= 20 continue
# 14 + 5 = 19
# Checking bound: 19 <= 20 continue
# 19 + 5 = 24
# Checking bound: 24 > 20 STOP!

# 30
# 26
# 2

	

# Enter the bound to stop: 30
# Enter initial number: 26
# Increased by: 2

# Here is the display:
# 26 + 2 = 28
# Checking bound: 28 <= 30 continue
# 28 + 2 = 30
# Checking bound: 30 <= 30 continue
# 30 + 2 = 32
# Checking bound: 32 > 30 STOP!

bound = int(input("Enter the bound to stop: "))
first = int(input("Enter initial number: "))
additive = int(input("Increased by: "))
print("\nHere is the display:")
sumAll = first
loop = True

while loop:
    if sumAll + additive <= bound:
        print(f"""{sumAll} + {additive} = {sumAll+additive}
Checking bound: {sumAll+additive} <= {bound} continue""" )
        sumAll += additive
    else:
        print(f"""{sumAll} + {additive} = {sumAll+additive}
Checking bound: {sumAll+additive} > {bound} STOP!""")
        break

        
        
