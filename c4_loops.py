"""
name="WafIa"
uppercase = 0
for char in name :
    if char.isupper() :
        uppercase = uppercase + 1
print(uppercase)
"""
"""
word=input("enter a word: ")
vowels = 0
for char in word:
    if char.lower() in word:
        vowels = vowels + 1
print(vowels)
"""
"""
word=input("enter a word: ")
vowels = 0
uppercase = 0
for char in word:
    if char.lower() in word:
        vowels = vowels + 1
for char in word :
    if char.isupper() :
        uppercase = uppercase + 1
print(vowels,uppercase)
"""
"""
sentence = input("Enter a sentence: ")
for i in range(len(sentence)) :
    if sentence[i].isupper() :
        print(i)
"""
"""
found = False
position = 0
sentence = input("Enter a sentence: ")

while not found and position < len(sentence):
    if sentence[position].isdigit():
        found = True
    else:
        position += 1

if found:
    print("First digit occurs at position", position)
else:
    print("The string does not contain a digit.")
"""
"""
found = False
sentence = input("Enter a sentence: ")
position = len(sentence) - 1
while not found and position >= 0 :
    if sentence[position].isdigit() :
        found = True
    else :
        position = position - 1
print(position)
"""
"""
string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
    if position == 0:
        valid = string[position] == "("
    elif position == 4 :
        valid = string[position] == ")"
    elif position == 8 :
        valid = string[position] == "-"
    else:
        valid = string[position].isdigit()
position = position + 1
if valid :
    print("The string contains a valid phone number.")
else:
    print("The string does not contain a valid phone number.")
"""
string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
    valid = ((position == 0 and string[position] == "(") or
             (position == 4 and string[position] == ")") or
             (position == 8 and string[position] == "-") or
             (position != 0 and position != 4 and position != 8  and
              string[position].isdigit())) 
position = position + 1
if valid :
    print("The string contains a valid phone number.")
else:
    print("The string does not contain a valid phone number.")