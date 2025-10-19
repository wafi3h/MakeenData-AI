"""
name = "Asma"

for i in name:
    print(i)
    
text= input("Enter Your Text: ")
for t in text:
    print(t)
"""
"""   
name = "Wafiah"
total=0
for k in range (5):
     total +=10
     print(k)
     print(total)
"""
"""
total = 0
name = "Ahmed"
for i in range(5):
    print(i, name[i])
"""
"""
name =input("Enter Your Name: ")
n = len(name)
for i in range(n):
    print(i , name[i])
"""
"""
n=0

for i in range(5,0-1,-1):#output=5,,4,3,2,1,0
    print(i)
"""
"""
for i in range(1, 10, 2):
    print(i)
"""
"""
balance = int(input("Enter Your Balance: "))
years = 5
rate = 0.05
for i in range (1,years+1):
  balance += (balance*rate)
  print(i,balance)
"""
"""
for i in "Wafiah":
    print(i, end="")
    #print("*",end="")
    print(101)
"""
"""
for i in range (1,5):
    for j in range(1,5):
        print(i**j, " ",end="")
        """
"""
for i in range (3):
    for j in range(4):
        print("*",end="")
    print()
print()

for i in range (4):
    for j in range(3):
        print("#", " ",end="")
    print()
"""
"""
for i in range(3):
    for j in range(5):
        if j % 2 == 1:
            print("*", end="")
        else:
           print("-", end="")
    print()
print()
"""
"""
for i in range(3):
    for j in range(5):
        if i % 2 == j % 2:
            print("*", end="")
        else:
           print(" ", end="")
    print()
"""
"""
for i in range (4):
    for i in range (i+1):
        print("*",end="")
    print()
print()
for i in range(4):
    for j in range(4 - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
"""
"""
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
"""