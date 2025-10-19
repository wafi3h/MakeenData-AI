total = 0.0
inputStr = input("Enter value: ")
count = 0

while inputStr != "" :
 value = float(inputStr)
 if value < 0:
     count = count + 1
     total = total + value
 inputStr = input("Enter value: ")

print(count,"\n",total)