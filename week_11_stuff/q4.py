letterdict = {
    'A': 'Apple',
    'B': 'Banana',
    'C': 'Cat',
    'D': 'Dog',
    'E': 'Elephant',
    'F': 'Fish',
    'G': 'Garden',
    'H': 'Hand',
    'I': 'Icicle',
    'J': 'Arthur',
    'K': 'Kangaroo',
    'L': 'Lion',
    'M': 'Monkey',
    'N': 'Nest',
    'O': 'Orange',
    'P': 'Pet',
    'Q': 'Queen',
    'R': 'Rose',
    'S': 'Sunflower',
    'T': 'Train',
    'U': 'Umbrella',
    'V': 'Van',
    'W': 'Watch',
    'X': 'X-rays',
    'Y': 'Yo-yo',
    'Z': 'Zebra'
}

word = input("Enter a name: ").upper()
print()
for i in range(len(word)):
    print(f"{i+1}. {word[i]} for {letterdict.get(word[i])}")
