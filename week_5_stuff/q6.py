# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567
# 12345678
# 123456789

for i in range(1,10):
    print(i)
    for j in range(i):
        if i < 9:
            print(f"{j + 1}", end='')
        else:
            break
      