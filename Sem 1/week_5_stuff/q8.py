# Input 	Result

# Wollongong
# U

	

# Enter something: Wollongong
# Upper or Lower (U/L): U
# index=0: 5 repeated letter WWWWW
# index=1: 5 repeated letter OOOOO
# index=2: 5 repeated letter LLLLL
# index=3: 5 repeated letter LLLLL
# index=4: 5 repeated letter OOOOO
# index=5: 5 repeated letter NNNNN
# index=6: 5 repeated letter GGGGG
# index=7: 5 repeated letter OOOOO
# index=8: 5 repeated letter NNNNN
# index=9: 5 repeated letter GGGGG

# FrOg
# L

	

# Enter something: FrOg
# Upper or Lower (U/L): L
# index=0: 5 repeated letter fffff
# index=1: 5 repeated letter rrrrr
# index=2: 5 repeated letter ooooo
# index=3: 5 repeated letter ggggg

word = input("Enter something: ").upper()
choice = input("Upper or Lower (U/L): ").upper()

if choice == "L":
    word = word.lower()

for i in range(len(word)):
    start = word[0 + i]
    print(f"index={i}: 5 repeated letter ", end="")
    for j in range(5):
        print(f"{start}", end="")
    print()