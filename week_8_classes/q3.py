# In the answer box, a code snippet of a class called Employee is given.

# Your task is to write the special method __str__ so that if we have an object
# employeeObj = Employee("012345", "John", "Smith", "Accountant", "1234")
# then str(employeeObj) will return the string 012345 John Smith

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
  # write method __str__ here
  def __str__(self):
    return f"{self.employee_id} {self.first_name} {self.last_name}"
  
  def __str__(self):
    return Employee(f"{self.employee_id} {self.first_name} {self.last_name}")

#}