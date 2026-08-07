# Dog
# 5

	

# Enter something: Dog
# How many lines? 5

# Here it is:
# line 1: D
# line 2: o
# line 3: g
# line 4: D
# line 5: o

# Wollongong
# 4

	

# Enter something: Wollongong
# How many lines? 4

# Here it is:
# line 1: W
# line 2: o
# line 3: l
# line 4: l

word = input("Enter something: ")
lines = int(input("How many lines? "))
print("\nHere it is:")
count = 0
lcount = 1

while lcount <= lines:
    if count >= len(word):
        count = 0
    char = word[0 + count]
    print(f"line {lcount}: {char}")
    count += 1
    lcount += 1