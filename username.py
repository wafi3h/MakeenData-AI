correct_username= "admin"
correct_password= 12345

name = input("Enter User Name: ")
password = input("Enter Password: ")

if name == correct_username and number == correct_password:
#if name == correct_username or number == correct_password:
#if name != correct_username and number != correct_password:
    print("Access denied")
else:
    print("Access granted")