# Write code to create a class called Staff and the method __init__ to initialise the following instance attributes in this order:
# -staff_number
# -first_name
# -last_name
# -email

class Staff:
    def __init__(self, staff_number, first_name, last_name, email):
        self.staff_number = staff_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        