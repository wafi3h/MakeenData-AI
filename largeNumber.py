larg_number = int(input("Enter a value: "))
inputStr = input("Enter a value: ")
 
while inputStr != "" :
    value = int(inputStr)
    if value > larg_number:
        larg_number = value
    inputStr = input("Enter a value: ")
print(larg_number)