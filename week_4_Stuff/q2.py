
def Receipt(method, items):
    if items <= 50:
        if method == "s":
            return "Standard post", 10
        elif method == "r":
            return "Registered post", 15
        elif method == "e":
            return "Express post", 20
    if items > 50:
        if method == "s":
            return "Standard post", 0
        elif method == "r":
            return "Registered post", 10
        elif method == "e":
            return "Express post", 17


items = int(input("Enter the number of items: "))
method = input("Enter shipping method (s/r/e): ")


if items <= 50:
    amount = items * 3
    post, postPrice = Receipt(method,items)
    print(f"""\nReceipt:
{items} items x $3 = ${amount}
{post}: ${postPrice}
Total: ${amount + postPrice}        
""")
elif items > 50:
    amount = items * 2
    post, postPrice = Receipt(method,items)
    print(f"""\nReceipt:
{items} items x $2 = ${amount}
{post}: ${postPrice}
Total: ${amount + postPrice}        
""")


