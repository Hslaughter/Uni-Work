# def expand(word, multiplicity):
#     result = ""
#     for i in range(0, len(word)):
#         letter = word[i]
#         lettermult = letter * multiplicity
#         result = result + lettermult
#     return result
    
# expanded_word = expand("frog", 2)
# print(expanded_word)

def factorial(n):
    if n== 1:
        return 1
    else:
        return n * factorial(n-1)
    
for i in range(1,10):
    print(f"{i}! = {factorial(i)}")

    
result = factorial(5)
print(result)