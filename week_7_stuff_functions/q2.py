def triple(sentence):
#{
  # initialise the result string to empty
  result = ""

  # go through each letter
  for i in range(0, len(sentence)):
  #{
    # get the ith letter
    letter = sentence[i]
    
    # add letter 3 times to the result
    result = result + (letter * 3)
  #}

  return result

inp = input("Enter a sentence: ")
result = triple(inp)
print(f"Triple effect: {result}")