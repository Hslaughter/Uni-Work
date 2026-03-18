print("Welcome to Ocean World.")
child = int(input("How many tickets for children under 6? "))
teen = int(input("How many tickets for children age between 6-17? "))
adult = int(input("How many tickets for adults? "))
total_tickets = child + teen + adult
cost_of_teen = teen * 7
cost_of_adult = adult * 20
total_cost = cost_of_adult + cost_of_teen

print("Receipt:")
print(f"Number of tickets: {total_tickets}")
print(f"Total cost ${total_cost}")