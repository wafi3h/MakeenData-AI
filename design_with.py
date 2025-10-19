for i in range(7):
    for j in range(7 - i + 1):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

for i in range(1,7):
    for j in range(i):
        print(" ", end="")
    for k in range(7 - j-1):
        print("*", end="")
    print()
