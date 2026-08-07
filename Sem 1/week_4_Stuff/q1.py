# Number of items 	Cost
# 1-50 	$3 per item
# Postage: $10
# More than 50 	$2 per item
# Postage: free
# Enter the number of items: 10

# Receipt: 
# 10 items x $3 = $30
# Postage: $10
# Total: $40

items = int(input("Enter the number of items: "))

if items < 50:
    postage = 10
    amount = items * 3
    newsum = amount + postage
    print(f"""
Receipt: 
{items} items x $3 = ${amount}
Postage: ${postage}
Total: ${newsum}
    """)
elif items > 50:
    postage = 0
    amount = (items * 2)
    print(f"""
Receipt: 
{items} items x $2 = ${amount}
Postage: ${postage}
Total: ${amount}
        """)

