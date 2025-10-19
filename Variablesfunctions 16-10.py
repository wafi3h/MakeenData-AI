"""
def main():
    sideLength = int(input("Enter a Number: "))
    result = cubeVolume(sideLength)
    return(result)
 
def cubeVolume(sideLength):
    return sideLength * sideLength * sideLength

res=main()
print(res)
"""
"""
# Other answer
def main(l):
    result = cubeVolume(l)
    return(result)
 
def cubeVolume(sideLength):
    return sideLength * sideLength * sideLength

length = int(input("Enter a Number: "))
print(main(length))
"""
"""
#This function intends to access the global ‘balance’ variable
balance = 10000
def withdraw(amount):
    global balance
    if balance >= amount:
        balance = balance - amount
withdraw(350)
print("balance = ", balance)
"""
"""
#List
name = "Wafiah"
trainAI = ["Azam","Noor","Muradi","Ali",name]#it can except varibale
contactNumber = ["3958455"]
number = [1,2,3,4,5,6]

mixList = ["Ahmed","Mune",5,4]

print(mixList)
print(number)
print(len(trainAI))
print(trainAI[3])
print(len(trainAI))
"""
"""
number = [2, 4, -2, 20, 4]
max_num = number[0]
min_num = number[0]
for i in number:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i
print("Maximum number is:", max_num)
print("Minimum number is:", min_num)
"""
"""
number = [2, 4, 5, 7, 6, 9]
for i in range(len(number)):
    if number[i] % 2==0:
        print("Even number is:",number[i])
    else:
        print("Odd number is:",number[i])
"""
"""
# convert digit to int
number = []

while True:
    newNum = input("Enter a number or 'q' to stop: ")
    if newNum == "q":
        break
    elif newNum.isdigit():
        number.append(int(newNum))
    else:
        number.append(newNum)
print("The list of numbers is:", number)
"""