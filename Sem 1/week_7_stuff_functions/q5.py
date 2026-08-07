def display_downward(start):
    while start >= 0:
        print(f"{start} ", end="")
        start -= 2
    

def display_pattern(line_count):
    for i in range(1,line_count+1):
        display_downward(i*2)
        print()
        
            


user_num = int(input("Enter starting number: "))
display_downward(user_num)

user_line = int(input("Enter line amount: "))
display_pattern(user_line)