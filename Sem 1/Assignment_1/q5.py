# Enter subject code: MATH111
# Enter subject title: Abstract Algebra
# Number of credit points: 5
# Cost per credit point: 200
# Is this a core subject (Y/N)? N

# Here is the output
# <<<
#   "code": "MATH111",
#   "title": "Abstract Algebra",
#   "core": "N",
#   "cp": 5,
#   "fee": 1000
# >>>
# gathering inputs from user and assigning to variables
subCode = input("Enter subject code: ")
subTitle = input("Enter subject title: ")
credit = int(input("Number of credit points: ")) # cast as int where needed
costPer = int(input("Cost per credit point: ")) # will be using int variables for computation
yOrn = input("Is this a core subject (Y/N)? ") # keep rest as strings
# use """" print statements to easily use syntax that usually would need escaping and keep formatting as is written
print(f"""\nHere is the output 
<<<
  "code": "{subCode}",
  "title": "{subTitle}",
  "core": "{yOrn}",
  "cp": {credit},
  "fee": {credit * costPer}
>>>""")
# use f-strings where needed and do computation within f-string to not have to make another variable

