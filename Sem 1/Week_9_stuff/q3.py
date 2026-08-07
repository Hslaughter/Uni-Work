# In the answer box, a code snippet of a class called Staff is given.

# Your task is to write the method print_details(self, width) so that if we have an object
# staffObj = Staff("012345", "John", "Smith", "js@gmail.com")
# then staffObj.print_details(40) will display the staff information in a box of width 40 as follows:
# Test 	Result

# staffObj = Staff("012345", "John", "Smith", "js@gmail.com")
# staffObj.print_details(40)

# ----------------------------------------
# | Staff number: 012345                 |
# | John Smith                           |
# | js@gmail.com                         |
# ----------------------------------------

class Staff:
#{
  def __init__(self, staff_number, first_name, last_name, email):
  #{
    self.staff_number = staff_number
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
  #} 
  
  def print_details(self, width):
  #{
    for i in range(width):
      print("-",end='')
    print(f"\n| Staff number: {self.staff_number:<{width - 4 - len('Staff number: ')}} |")
    print(f"| {self.first_name} {self.last_name:<{width - 4 - len(self.first_name) - 1}} |")
    print(f"| {self.email:<{width - 4}} |")
    for i in range(width):
      print("-",end='')
    
  #}
#}
staffObj = Staff("012345", "John", "Smith", "js@gmail.com")
staffObj.print_details(40)