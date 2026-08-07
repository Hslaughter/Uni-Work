# Using the following variables:

# product_code = "377B"
# product_name = "Beef Liquid Stock"
# product_size = "250mL"
# product_price = 2.15

# a) Write one print statement using the above variables and string addition so that it produces the following exact output:
# 377B: Beef Liquid Stock, 250mL

# b) Write one print statement using the above variables and string addition so that it produces the following exact output:
# Beef Liquid Stock, 250mL, $2.15

# c) Write one print statement using the above variables and string format so that it produces the following exact output:
# 377B: Beef Liquid Stock, 250mL

# d) Write one print statement using the above variables and string format so that it produces the following exact output:
# Beef Liquid Stock, 250mL, $2.15

product_code = "377B"
product_name = "Beef Liquid Stock"
product_size = "250mL"
product_price = 2.15

print(f"{product_code}: {product_name}, {product_size}")

print(f"{product_name}, {product_size}, ${product_price}")

print(f"{product_code}: {product_name}, {product_size}")

print(f"{product_name}, {product_size}, ${product_price}")