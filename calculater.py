while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print("Please select operation -\n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "5. Exit\n")
    
    sel = int(input("Select operation (1-5): "))
    
    if sel == 1:
        print("The addition of", num1, "+", num2, "=", num1 + num2)
    elif sel == 2:
        print("The subtraction of", num1, "-", num2, "=", num1 - num2)
    elif sel == 3:
        print("The multiplication of", num1, "*", num2, "=", num1 * num2)
    elif sel == 4:
        if num2 != 0:
            print("The division of", num1, "/", num2, "=", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    elif sel == 5:
        print("Exiting the program. Goodbye!")
        break
else:
        print("Invalid operator. Please try again.")
    
print("\n") 