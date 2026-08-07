# Input 	Result

# 13

	

# Enter the initial number: 13
# Sequence:
# Step 0: 13
# Step 1: 28
# Step 2: 85
# Step 3: 172


def next_number(number):
#{
  if (number%2 == 0):
    return 3 * number + 1
  else:
    return 2 * number + 2   
#}

num = int(input("Enter the initial number: "))
print("Sequence: ")
print(f"Step 0: {num}")
result = num
step = 1

while num <= 100:
  new = next_number(num)
  print(f"Step {step}: {new}")
  step += 1
  num = new
