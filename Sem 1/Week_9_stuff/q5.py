# Test 	Result

# PrintUtil.display_numbers(min_num=2, max_num=7, separator="$", ending=".")
# PrintUtil.display_numbers(min_num=4, max_num=4, separator="$", ending=".")

	

# 2$3$4$5$6$7.
# 4.

class PrintUtil:
    def __init__(self):
        pass

    @staticmethod
    def display_numbers(min_num, max_num, separator, ending):
        result = ""
        for i in range(min_num,max_num+1):
            if result != "":
                result += f"{separator}"
            result += f"{min_num}"
            min_num += 1
        result+= f"{ending}"
        print(result)

PrintUtil.display_numbers(min_num=2, max_num=7, separator="$", ending=".")
PrintUtil.display_numbers(min_num=4, max_num=4, separator="$", ending=".")