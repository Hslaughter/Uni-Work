# A dictionary is given in the answer box. Using this dictionary, write code to print out Queensland and Victoria.
state_abb = {
  "NSW": "New South Wales",
  "ACT": "Australian Capital Territory",
  "NT": "Northern Territory",
  "QLD": "Queensland",
  "SA": "South Australia",
  "TAS": "Tasmania",
  "VIC": "Victoria",
  "WA": "Western Australia"
}

print(f"{state_abb.get("QLD")} {state_abb.get("VIC")}")