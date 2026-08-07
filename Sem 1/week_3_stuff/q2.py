# Enter number of cows to purchase: 1
# Enter number of ducks to purchase: 3
# Enter number of chicken to purchase: 4
# Cost: 
# 1 cow = 30 grassies
# 3 duck = 15 grassies
# 4 chick = 12 grassies
# Total = 57 grassies

cow = int(input("Enter number of cows to purchase: "))
cows = cow * 30
duck = int(input("Enter number of ducks to purchase: "))
ducks = duck * 5
chicken = int(input("Enter number of chicken to purchase: "))
chickens = chicken * 3

Total = cows + ducks + chickens

print(f"""Cost:
{cow} cow = {cows} grassies
{duck} duck = {ducks} grassies
{chicken} chick = {chickens} grassies
Total = {Total} grassies
""")
