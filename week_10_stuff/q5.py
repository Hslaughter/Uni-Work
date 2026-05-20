# Study the examples below and write a program that works exactly like the examples. Your program should be written in a way to make it easy to add more journals in the future.

# For example:
# Input 	Result

# Y
# N
# N
# Y
# N

	

# We offer the following journals:
# Select JAA $30? (Y/N): Y
# Select JBN $50? (Y/N): N
# Select JHK $45? (Y/N): N
# Select JUR $28? (Y/N): Y
# Select JMS $100? (Y/N): N
# Selected journals: JAA, JUR
# Total cost: $58


journals = {
    "JAA": 30,
    "JBN": 50,
    "JHK": 45,
    "JUR": 28,
    "JMS": 100
}

selected = []
total = 0
print("We offer the following journals:")
for journal, price in journals.items():
    choice = input(f"Select {journal} ${price}? (Y/N): ").upper()

    if choice == "Y":
        selected.append(journal)
        total += price
if not selected:
    print("Selected journals: None")
else: 
    print("Selected journals: ", end="")
    print(*selected, sep=", ")
    print(f"Total cost: ${total}")
