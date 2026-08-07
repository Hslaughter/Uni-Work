# Write code to create a class called Employee and the method __init__ to initialise the following instance attributes in this order:
# -employee_id
# -first_name
# -last_name
# -position
# -phone

class Employee:
    def __init__(self, employee_id, first_name, last_name, position, phone):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.phone = phone