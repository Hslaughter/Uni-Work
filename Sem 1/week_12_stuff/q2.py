# A subject has 3 assessments:
# - An assignment whose mark is an integer between 0 and 20;
# - A project whose mark is an integer between 0 and 30;
# - A final exam whose mark is an integer between 0 and 50.

# Write a program to ask user to enter assessment marks and display total mark.
# The program should stop when there is an error and display that error.
# The program must use the function get_assessment_mark provided in the answer box.

# For example:
# Input 	Result

# 10
# 25
# 40

	

# Enter assignment mark (0-20): 10
# Enter project mark (0-30): 25
# Enter final exam mark (0-50): 40
# Total mark: 75

# 30

	

# Enter assignment mark (0-20): 30
# Error: assignment mark must be between 0 and 20

# frog

	

# Enter assignment mark (0-20): frog
# Error: assignment mark is invalid

def get_assessment_mark(assessment_name, mark_min, mark_max):
#{
  """
  Ask user to enter assessment mark and return the mark.
  Raise ValueError if one of the following occurs:
  - mark is not an integer
  - mark is out of range
  """

  # ask user to enter mark
  user_input = input("Enter {0} mark ({1}-{2}): "
    .format(assessment_name, mark_min, mark_max))

  # check if mark is integer
  try:
    mark = int(user_input)
  except ValueError as e:
    raise ValueError("{0} mark is invalid".format(assessment_name))    

  # check mark between max and min
  if (mark > mark_max):
    raise ValueError("{0} mark must be between {1} and {2}"
      .format(assessment_name, mark_min, mark_max))

  if (mark < mark_min):
    raise ValueError("{0} mark must be between {1} and {2}"
      .format(assessment_name, mark_min, mark_max))

  return mark
#}

# write your code here
try:
    assmark = get_assessment_mark('assignment', 0, 20)
    projmark = get_assessment_mark('project', 0, 30)
    exam_mark = get_assessment_mark('final exam', 0, 50)
    total = assmark + projmark + exam_mark
    print(f"Total mark: {total}")
except ValueError as e:
    print(f"Error: {e}")
    
   
