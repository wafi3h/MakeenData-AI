"""
values = [1, 16, 9, 4]
values.sort()
print(values)
"""
"""
values = [1, 16, 9, 4]
values.sort(reverse = True)
print(values)
"""
"""
lis = [1,2,3,4]#list wrote in the memory
newLis=lis#newList take the same variable in lis
lis.append(5)#adding new value
lis.append(6)#adding new value
newLis=list(lis)   
print(newLis)
# coping the list
"""
"""
slices the list
lis = [1,2,3,4,5,6,7,8,9]
mylist = lis[2:8]#it will take the value in indext 2 , but the value befor indext 8
print(mylist)
"""
"""
#for negetive number
#if number with string it should print it as string
lis = []
while True:
  inputStr = input("Enter Number: ")
  
  if inputStr.isdigit():
      lis.append(int(inputStr))
      
  elif inputStr[0] == "-" and inputStr[1:].isdigit():
      lis.append(int(inputStr[1:]) * -1)
      
  elif inputStr == "q":
        break
  else:
      lis.append(inputStr)
print(lis)
"""
"""
#git the positive number and negative number without using isdigit
lisPositive = []
lisNegative=[]
while True:
  inputStr = input("Enter Number: ")
  if inputStr == "q":
      break
  else:
      inputStr = int(inputStr)
      if inputStr >=0:
          lisPositive.append(inputStr)
              
      else:
          lisNegative.append(inputStr)
          
print(lisPositive,lisNegative)
###OTHER ANWSER###
lisPositive = []
lisNegative=[]
while True:
  inputStr = input("Enter Number: ")
  if inputStr == "q":
      break
  if inputStr.isdigit():
      inputStr = int(inputStr)
      lisPositive.append(inputStr)
              
  elif inputStr[0] == "-":
      inputStr = int(inputStr[1:]) * -1
      lisNegative.append(inputStr)

print(lisPositive,lisNegative)
"""
"""
#git the sum of number
lis = []

while True:
    inputStr = input("Enter Number: ")
    if inputStr == "done":
        break
    else:
        lis.append(int(inputStr))
print("Sum:", sum(lis))
#other Answer
lis = []

while True:
    inputStr = input("Enter Number: ")
    if inputStr == "done":
        break
    elif inputStr.lstrip("-").isdigit():
        lis.append(int(inputStr))
print("Sum:", sum(lis))
"""