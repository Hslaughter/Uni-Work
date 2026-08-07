# Write a function based on the following specification.
# Function name: 	get_assessment_mark
# Input arguments: 	3 arguments:

#     assessment_name: a string,
#     mark_min: an integer, the minimum mark,
#     mark_max: an integer, the maximum mark

# Return values: 	Return 1 integer value.
# The function asks the user to enter a mark and return this mark.
# Exception: 	Raise ValueError if one of the following error occurs:

#     Mark is not an integer,
#     Mark is not between the range

# Example: 	If assessment_name = Assignment 1, mark_min = 0, mark_max = 20 then the function prompts the user with "Enter Assignment 1 mark (0-20): "

# If the user enters a non-integer then an exception ValueError is raised with the message "Assignment 1 mark is invalid"

# If the user enters a mark that is not between the correct range then an exception ValueError is raised with the message "Assignment 1 mark must be between 0 and 20"

# If the user enters an integer mark between the correct range then the function returns this mark.

def get_assessment_mark(assessment_name, mark_min, mark_max):
    try:
        assmark = int(input(f"Enter {assessment_name} mark ({mark_min}-{mark_max}): "))   
    except ValueError:
        raise ValueError(f"{assessment_name} mark is invalid")
    if assmark < mark_min or assmark > mark_max:
        raise ValueError(f"{assessment_name} mark must be between {mark_min} and {mark_max}") 
    if assmark >= mark_min and assmark <= mark_max:
            return assmark
    
 	

try:
  result = get_assessment_mark("Quiz 4", 0, 50)
  print(result)
except ValueError as e:
  print(e)