# display_pattern(word="sydney")

	

# index 0: s 1 s 2 s 3
# index 1: y 2 y 3 y 4
# index 2: d 3 d 4 d 5
# index 3: n 4 n 5 n 6
# index 4: e 5 e 6 e 7
# index 5: y 6 y 7 y 8

# index 0: s 1 s 2 s 3
# index 1: y 2 y 3 y 4
# index 2: d 3 d 4 d 5
# index 3: n 4 n 5 n 6
# index 4: e 5 e 6 e 7
# index 5: y 6 y 7 y 8

# display_pattern(word="hi")

	

# index 0: h 1 h 2 h 3
# index 1: i 2 i 3 i 4

def display_pattern(word):
 
    for i in range(len(word)):
        one = i + 1
        two = i + 2
        three = i + 3
        print(f"index {i}: {word[i]} {one} {word[i]} {two} {word[i]} {three}")

display_pattern(word="sydney")
# display_pattern(word="hi")