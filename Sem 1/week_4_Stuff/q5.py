journals = {
    "JAA": 30,
    "JBN": 50,
    "JHK": 45,
    "JUR": 28
}

selected = []
total = 0
print("We offer 4 journals: JAA, JBN, JHK and JUR")
for journal, price in journals.items():
    choice = input(f"Select {journal} ${price}? (Y/N): ").upper()

    if choice == "Y":
        selected.append(journal)
        total += price

if selected:
    print(f"Selected journals: {', '.join(selected)}")
    print(f"Total cost: ${total}")
else:
    print("Selected journals: None")
