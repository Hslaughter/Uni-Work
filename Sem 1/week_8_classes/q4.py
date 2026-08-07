# In the answer box, a code snippet of a class called Employee is given.

# Your task is to write the special method __repr__ so that if we have an object
# employeeObj = Employee("012345", "John", "Smith", "Accountant", "1234")
# then repr(employeeObj) will return the string
# Employee('012345', 'John', 'Smith', 'Accountant', '1234')

class Employee:
#{
  def __init__(self, employee_id, first_name, last_name, position, phone):
  #{
    self.employee_id = employee_id
    self.first_name = first_name
    self.last_name = last_name
    self.position = position
    self.phone = phone
  #} 
  # write method __repr__ here
  def __repr__(self):
    return f"Employee({self.employee_id!r} {self.first_name!r} {self.last_name!r} {self.position!r} {self.phone!r})"
#}