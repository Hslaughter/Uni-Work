# PrintUtil.display_timestable(multiplier=7)

# 1 x 7 = 7
# 2 x 7 = 14
# 3 x 7 = 21
# 4 x 7 = 28
# 5 x 7 = 35
# 6 x 7 = 42
# 7 x 7 = 49
# 8 x 7 = 56
# 9 x 7 = 63
# 10 x 7 = 70

class PrintUtil:
    def __init__(self,):
        pass
    @staticmethod
    def display_timestable(multiplier):   
        for i in range(1,11):
            print(f"{i} x {multiplier} = {i*multiplier}")

PrintUtil.display_timestable(multiplier=7)