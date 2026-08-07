lines = int(input("How many lines? "))
print()
print("Here it is:")
for i in range(lines):
    start = 10 + i
    for j in range(i+2):
        if j > 0:
            print("<", end=" ")
        print(start + j, end=" ")
    print()
        
        
        



