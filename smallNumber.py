inputStr = input("Enter a value: ")
small_number = int(inputStr)

while inputStr != "" :
    value = int(inputStr)
    if value < small_number:
        small_number = value
    inputStr = input("Enter a value: ")
print(small_number)
