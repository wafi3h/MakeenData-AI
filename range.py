for i in range (4):
    for i in range (i+1):
        print("*",end="")
    print()
print()
for i in range(4):
    for j in range(4 - i- 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
print()

