# Use a dictionary to write a program that works exactly like the following example.

# For example:
# Input 	Result

# NT

	

# Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: NT
# The state you entered is Northern Territory

state_map = {
  "NSW": "New South Wales",
  "ACT": "Australian Capital Territory",
  "NT": "Northern Territory",
  "QLD": "Queensland",
  "SA": "South Australia",
  "TAS": "Tasmania",
  "VIC": "Victoria",
  "WA": "Western Australia"
}

userinp = input("Enter state NSW/ACT/NT/QLD/SA/TAS/VIC/WA: ").upper()
if userinp in state_map.keys():
    print(f"The state you entered is {state_map.get(userinp)}")