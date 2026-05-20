# These are the Italian words for 0-9: zero, uno, due, tre, quattro, cinque, sei, sette, otto, nove.

# Write a program to translate italian words into numerical code. The program must work exactly like the following example.

# For example:
# Input 	Result

# due-zero-due-sei

	

# Please enter italian: due-zero-due-sei
# You have entered: 2026

italian = {
    'zero': "0",
    'uno': "1",
    'due': "2",
    'tre': "3",
    'quattro': "4",
    'cinque': "5",
    'sei': "6",
    'sette': "7",
    'otto': "8",
    'nove': "9"
}

userinp = input("Please enter italian: ").lower()
result=""
while True:
    hyphen = userinp.find("-") # due-zero-due-sei
    if hyphen == -1: # due
        result += italian.get(userinp)
    else:
        first = userinp[:hyphen] # due
        result += italian.get(first)
        second = userinp[hyphen+1:] # zero-due-sei
        userinp = second