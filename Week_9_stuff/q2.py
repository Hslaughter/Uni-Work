# In the answer box, a code snippet of a class called Staff is given.

# Your task is to write code to create 3 Staff objects with the following details:

# staffObj1: 100001, John, Lee, jl123@gmail.com
# staffObj2: 100002, Mary, Zheng, maryz@gmail.com
# staffObj3: 100003, Cindy, Wilson, cw456@hotmail.com

class Staff:
#{
  def __init__(self, staff_number, first_name, last_name, email):
  #{
    self.staff_number = staff_number
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
  #} 
#}

# write your code to create objects:
#staffObj1: 100001, John, Lee, jl123@gmail.com
#staffObj2: 100002, Mary, Zheng, maryz@gmail.com
#staffObj3: 100003, Cindy, Wilson, cw456@hotmail.com

staffObj1 = Staff(100001,'John','Lee','jl123@gmail.com')
staffObj2 = Staff(100002,'Mary','Zheng','maryz@gmail.com')
staffObj3 = Staff(100003,'Cindy','Wilson','cw456@hotmail.com')